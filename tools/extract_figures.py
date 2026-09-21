"""抽圖工具：把手冊 Markdown 裡的『［圖 X-Y．中文圖說］原文圖說：Figure X-Y. ...』
文字佔位，換成 <figure> 區塊，圖片以 PyMuPDF 依版面座標從原始 PDF 重新渲染。

用法（範例，TC 3-21.76）：
    python3 tools/extract_figures.py \
        --pdf TC_3-21.76/TC_3-21.76_Ranger_Handbook_September_2025.pdf \
        --docname TC 3-21.76 \
        --outdir docs/public/images/ranger-handbook \
        --imgpath /images/ranger-handbook \
        docs/ranger-handbook/*.md

做法：單次掃描全書，找出每一行「行首」是 `Figure X-Y.` 的 caption，
記錄其所在頁與行的 bbox；再找該 caption 正上方、水平位置相近（或該頁只有
一張圖）的圖片 bbox，兩者的垂直間距即用來判斷是否為同一張圖的圖說。
比對結果會印出，供人工抽查後再實際渲染／替換（渲染前建議先跑
--dry-run 看比對是否合理）。
"""
import argparse
import glob
import json
import re
import sys
from collections import defaultdict

import fitz  # pymupdf

PLACEHOLDER_RE = re.compile(
    r'^> \*\*［圖\s*([0-9A-Za-z]+-[0-9A-Za-z]+)．(.+?)］\*\*　原文圖說：'
    r'(Figure\s+[0-9A-Za-z]+-[0-9A-Za-z]+\.\s*.+)$'
)
CAPTION_LINE_RE = re.compile(r'^Figure\s+([0-9A-Za-z]+-[0-9A-Za-z]+)\.\s*(.*)$')


def parse_placeholders(md_files):
    placeholders = []
    for path in md_files:
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        for i, line in enumerate(lines, start=1):
            if "［圖" not in line:
                continue
            m = PLACEHOLDER_RE.match(line.strip())
            if not m:
                print(f"!! 格式不符：{path}:{i}  {line.strip()[:80]}", file=sys.stderr)
                continue
            fid, zh, en_full = m.groups()
            placeholders.append({
                "file": path, "line": i, "fid": fid,
                "zh": zh, "en_full": en_full.strip(),
            })
    return placeholders


def scan_pdf(doc, footer_re):
    """單次掃描全書，回傳 (by_fid, page_images, page_footer)。"""
    by_fid = defaultdict(list)
    page_images, page_footer = {}, {}
    for pno in range(len(doc)):
        page = doc[pno]
        page_images[pno] = page.get_image_info()
        txt = page.get_text()
        m = re.search(footer_re, txt)
        page_footer[pno] = m.group(1) if m else None
        d = page.get_text("dict")
        for block in d["blocks"]:
            if block.get("type") != 0:
                continue
            for line in block.get("lines", []):
                text = "".join(s["text"] for s in line["spans"]).strip()
                mm = CAPTION_LINE_RE.match(text)
                if mm:
                    by_fid[mm.group(1)].append({
                        "page": pno, "bbox": line["bbox"], "text": text,
                    })
    return by_fid, page_images, page_footer


def find_image_bbox(cap_bbox, images):
    x0, y0, x1, y1 = cap_bbox
    best = None
    for im in images:
        ix0, iy0, ix1, iy1 = im["bbox"]
        gap = y0 - iy1
        if 0 <= gap < 90:
            cap_cx, im_cx = (x0 + x1) / 2, (ix0 + ix1) / 2
            overlap = not (ix1 < x0 - 5 or ix0 > x1 + 5)
            close = abs(cap_cx - im_cx) < 100
            if overlap or close or len(images) == 1:
                if best is None or gap < best[0]:
                    best = (gap, (ix0, iy0, ix1, iy1))
    return best


def match_all(placeholders, by_fid, page_images, page_footer):
    resolved, unresolved = [], []
    for p in placeholders:
        occs = sorted(by_fid.get(p["fid"], []), key=lambda o: -o["page"])
        chosen = None
        for o in occs:
            best = find_image_bbox(o["bbox"], page_images[o["page"]])
            if best:
                chosen = {
                    "page": o["page"], "cap_text": o["text"],
                    "image_bbox": best[1], "gap": best[0],
                    "printed_page": page_footer.get(o["page"]),
                }
                break
        if chosen:
            resolved.append({**p, **chosen})
        else:
            unresolved.append(p)
    return resolved, unresolved


def fname_for(fid):
    ch, seq = fid.split("-")
    m = re.match(r'(\d+)([A-Za-z]?)$', seq)
    seq_num, letter = (m.group(1), m.group(2).lower()) if m else (seq, "")
    stem = ch.lower() if ch.isalpha() else f"{int(ch):02d}"
    return f"fig-{stem}-{int(seq_num):02d}{letter}.png"


def render_all(doc, resolved, outdir, dpi=200):
    import os
    os.makedirs(outdir, exist_ok=True)
    manifest = []
    for r in resolved:
        page = doc[r["page"]]
        rect = fitz.Rect(*r["image_bbox"])
        mat = fitz.Matrix(dpi / 72, dpi / 72)
        pix = page.get_pixmap(clip=rect, matrix=mat)
        fn = fname_for(r["fid"])
        pix.save(os.path.join(outdir, fn))
        manifest.append({
            "fid": r["fid"], "page": r["page"], "file": fn,
            "w": pix.width, "h": pix.height,
            "caption": r["cap_text"], "printed": r["printed_page"],
        })
        r["file"] = fn
    json.dump(manifest, open(os.path.join(outdir, "_manifest.json"), "w", encoding="utf-8"),
               ensure_ascii=False, indent=1)
    return manifest


def replace_placeholders(resolved, imgpath):
    by_file = defaultdict(list)
    for r in resolved:
        by_file[r["mdfile"]].append(r)
    for path, entries in by_file.items():
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        by_line = {e["line"]: e for e in entries}
        out = []
        for idx, line in enumerate(lines, start=1):
            if idx in by_line:
                e = by_line[idx]
                m = PLACEHOLDER_RE.match(line.rstrip("\n"))
                if not m or m.group(1) != e["fid"]:
                    raise SystemExit(f"不吻合！{path}:{idx}")
                fid, zh, en_full = m.groups()
                out.append(
                    f'<figure>\n'
                    f'  <img src="{imgpath}/{e["file"]}" alt="圖 {fid}．{zh}" />\n'
                    f'  <figcaption>圖 {fid}．{zh}（原書 p.{e["printed_page"]}）<br />'
                    f'原文圖說：{en_full}</figcaption>\n'
                    f'</figure>\n'
                )
            else:
                out.append(line)
        with open(path, "w", encoding="utf-8") as fh:
            fh.writelines(out)
        print(f"{path}: 換了 {len(entries)} 處")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md_files", nargs="+")
    ap.add_argument("--pdf", required=True)
    ap.add_argument("--outdir", required=True, help="圖片輸出目錄")
    ap.add_argument("--imgpath", required=True, help="Markdown 裡 <img src> 的絕對路徑前綴")
    ap.add_argument("--dpi", type=int, default=200)
    ap.add_argument("--dry-run", action="store_true", help="只比對不渲染、不改檔")
    args = ap.parse_args()

    md_files = []
    for pattern in args.md_files:
        md_files.extend(sorted(glob.glob(pattern)))

    doc = fitz.open(args.pdf)
    doc_id_guess = re.search(r'([A-Z]{1,3}\s*\d[\d.\-]*)', args.pdf)
    footer_re = r'(?:' + re.escape(doc_id_guess.group(1)) + r')?\s*\n?\s*([0-9]+-[0-9]+|[A-Za-z]-[0-9]+)'

    placeholders = parse_placeholders(md_files)
    print(f"解析到 {len(placeholders)} 個佔位")

    by_fid, page_images, page_footer = scan_pdf(doc, footer_re)
    resolved, unresolved = match_all(placeholders, by_fid, page_images, page_footer)
    print(f"配對成功 {len(resolved)}，未解決 {len(unresolved)}")
    for u in unresolved:
        print("  未解決：", u["fid"], u["file"], u["line"])

    if args.dry_run:
        return

    for r in resolved:
        r["mdfile"] = r["file"]
    manifest = render_all(doc, resolved, args.outdir, args.dpi)
    print(f"渲染完成，共 {len(manifest)} 張")
    replace_placeholders(resolved, args.imgpath)


if __name__ == "__main__":
    main()
