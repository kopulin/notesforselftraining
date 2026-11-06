# AGENTS.md — notesforselftraining

軍事／技術文件翻譯專案。任何 agent 接手前先讀完本文件。
完整規則見 [`CLAUDE.md`](CLAUDE.md)，父層共用規則見 [`/Projects/CLAUDE.md`](../CLAUDE.md)；衝突時以 `CLAUDE.md` >父層為準。

---

## 專案定位

**產品：** 把英文原版文件（PDF）逐章翻譯成繁體中文 Markdown，並保留原書的圖片與版面對應關係。
**範圍：** 本 repo 同時放翻譯內容（PDF、`.md` 譯文、圖片、術語表）**與**發佈用的 VitePress 網站（`docs/`、主題、部署設定），比照 [`/Projects/tccc-notes/`](../tccc-notes/)。`docs/` 內的 Markdown 與圖片為單一事實來源。（2026-08-29 決策，取代舊「另開 repo」規則）
**Git Remote：** `https://github.com/kopulin/notesforselftraining.git`（2026-11-07 由 `Document_Traslate` 改名，網站網址 `https://kopulin.github.io/notesforselftraining/`）
**語言：** 所有回覆與交付文件使用繁體中文，專有名詞、軍語、藥名保留英文原文並在首次出現時加註中文。

---

## 目前進度

| 文件 | 位置 | 狀態 |
|------|------|------|
| ATP 4-02.11《Casualty Response (TCCC and First Aid)》 | 譯文 [`docs/atp-4-02.11/`](docs/atp-4-02.11/)　原始 PDF [`ATP_4-02.11/`](ATP_4-02.11/) | 翻譯完成，網站已架設 |
| TC 3-21.76《Ranger Handbook》 | 譯文 [`docs/ranger-handbook/`](docs/ranger-handbook/)　原始 PDF [`TC_3-21.76/`](TC_3-21.76/) | 翻譯完成，網站已架設，**145 張圖片已抽出並嵌入**（2026-09-20），待逐章內容驗收 |

ATP 4-02.11 章節（檔案欄為架站後的 canonical 檔名）：

| 章 | 檔案（`docs/atp-4-02.11/`） | 狀態 |
|----|------|------|
| Ch01 | `01-casualty-response.md` | 已翻譯 |
| Ch02 | `02-extraction-movement.md` | 已翻譯 |
| Ch03 | `03-tccc-fundamentals.md` | 已翻譯 |
| Ch04 | `04-massive-bleeding.md` | 已翻譯 |
| Ch05 | `05-airway.md` | 已翻譯 |
| Ch06 | `06-respiration-ventilation.md` | 已翻譯 |
| Ch07 | `07-circulation.md` | 已翻譯 |
| Ch08 | `08-hypothermia.md` | 已翻譯 |
| Ch09 | `09-secondary-assessment.md` | 已翻譯 |
| Ch10 | `10-eye-trauma.md` | 已翻譯 |
| Ch11 | `11-head-injury.md` | 已翻譯 |
| Ch12 | `12-burns.md` | 已翻譯 |
| Ch13 | `13-fractures-splinting.md` | 已翻譯 |
| Ch14 | `14-other-field-techniques.md` | 已翻譯 |
| Ch15 | `15-monitoring-evac-prep.md` | 已翻譯 |
| Ch16 | `16-bites-stings.md` | 已翻譯 |
| Ch17 | `17-environmental-injuries.md` | 已翻譯 |
| Ch18 | `18-sickle-cell-trait.md` | 已翻譯 |
| Ch19 | `19-cbrn-first-aid.md` | 已翻譯 |
| Ch20 | `20-combat-operational-stress.md` | 已翻譯 |
| 附錄 A | `app-a-aid-kits-amal.md` | 已翻譯 |
| 附錄 B | `app-b-rescue-equipment.md` | 已翻譯 |
| — | `docs/errata.md` | 原文勘誤彙整（28 處），隨站發佈 |

> **進度：20／20 章 + 2／2 附錄　＝　文字翻譯全部完成　｜　累計約 27.0 萬字**
> ✅ 2026-08-28 全書文字部分已無缺漏。
> ✅ **P1｜全書圖片已抽取完成**（2026-08-29）——109 張 200 dpi PNG 存於 `docs/public/images/atp-4-02.11/`，109 處佔位全數轉為 `<figure>` 區塊。
> ✅ **P2｜VitePress 網站已架設**（2026-08-29 第七場）——譯文搬入 `docs/atp-4-02.11/`（slug 檔名 + frontmatter），80 處 WARNING/CAUTION/IMPORTANT 轉 `::: danger`/`::: warning`，圖片路徑轉絕對路徑，`config.ts`／`index.md`／IBM Carbon 主題（含列印 CSS）／`deploy.yml`／`package.json` 全部到位。`npm run docs:build` 通過、本機預覽驗過。
> ⏳ 剩 P3：合併術語表、譯文逐章內容驗收（機器驗證都過，內容層面未經使用者確認）、GitHub Pages 首次啟用。
> ℹ️ 2026-08-29 發佈架構定案：單一 repo + VitePress，詳見 DEVLOG 第五場。
> ✅ **2026-09-18 首頁分流完成**：`docs/index.md` 改為手冊選單（2 張卡片），ATP 首頁搬到 `docs/atp-4-02.11/index.md`，新增 `docs/ranger-handbook/`（TC 3-21.76，19 個檔案：前言＋Ch01–15＋附錄 A/B＋詞彙表＋自己的 index.md）。`config.ts` 的 `sidebar` 改為依路徑分流的物件（`/atp-4-02.11/`、`/errata`、`/ranger-handbook/` 各自一份），`nav`／`title`／`footer` 改為涵蓋兩份手冊的中性文案。TC 章節內 6 處 WARNING／CAUTION／DANGER blockquote 一併轉為 VitePress container（DANGER 比照 WARNING 用 `::: danger`），NOTE 維持 blockquote。`npm run docs:build` 通過，本機預覽確認側欄分流與 container 樣式正確。
> ✅ **2026-09-20 TC 3-21.76 全書抽圖完成**：145 張 200 dpi PNG 存於 `docs/public/images/ranger-handbook/`，145 處佔位全數轉為 `<figure>` 區塊。做法比照 ATP：以 PyMuPDF 掃描全書比對「Figure X-Y.」行首 caption 與其上方圖片 bbox（單次掃描全書建索引，而非逐張搜尋，387 頁全書 <10 秒），驗收（`grep`　`［圖`　0 殘留、`<figure>`／`<img>`／`<figcaption>`／`</figure>` 標籤數四者相等、145 張圖檔＝145 處引用、無重複配對）全數通過。`docs/index.md`／`docs/ranger-handbook/index.md` 免責文案同步更新為「圖片已完成」。

原始 PDF：`ATP_4-02.11/ATP_4-02.11_Casualty_Response_TCCC_and_First_Aid_March_2026.pdf`（不進 `docs/`）

TC 3-21.76 章節（2025 年 9 月 19 日版，共 380 頁；PDF 頁為檔案實際頁碼）：

| 章 | 原書章名 | PDF 頁 | 狀態 |
|----|---------|--------|------|
| 前言 | Preface／Introduction → `TC_3-21.76_Ch00_前言與導言_zh-TW.md` | 17–24 | 已翻譯，待驗收 |
| Ch01 | Leadership → `TC_3-21.76_Ch01_領導_zh-TW.md` | 25–34 | 已翻譯（術語已驗收） |
| Ch02 | Operations → `TC_3-21.76_Ch02_作戰_zh-TW.md` | 35–80 | 已翻譯，待驗收 |
| Ch03 | Fire Support → `TC_3-21.76_Ch03_火力支援_zh-TW.md` | 81–100 | 已翻譯，待驗收 |
| Ch04 | Communications → `TC_3-21.76_Ch04_通訊_zh-TW.md` | 101–108 | 已翻譯，待驗收 |
| Ch05 | Demolitions → `TC_3-21.76_Ch05_爆破_zh-TW.md` | 109–118 | 已翻譯（特殊處理），待驗收 |
| Ch06 | Movement → `TC_3-21.76_Ch06_行進_zh-TW.md` | 119–136 | 已翻譯，待驗收 |
| Ch07 | Patrols → `TC_3-21.76_Ch07_巡邏_zh-TW.md` | 137–168 | 已翻譯，待驗收 |
| Ch08 | Battle Drills → `TC_3-21.76_Ch08_戰鬥演練_zh-TW.md` | 169–202 | 已翻譯，待驗收 |
| Ch09 | Military Mountaineering → `TC_3-21.76_Ch09_軍事登山_zh-TW.md` | 203–232 | 已翻譯，待驗收 |
| Ch10 | Machine Gun Employment → `TC_3-21.76_Ch10_機槍運用_zh-TW.md` | 233–248 | 已翻譯，待驗收 |
| Ch11 | Urban Operations → `TC_3-21.76_Ch11_城鎮作戰_zh-TW.md` | 249–258 | 已翻譯，待驗收 |
| Ch12 | Waterborne Operations → `TC_3-21.76_Ch12_水上作戰_zh-TW.md` | 259–280 | 已翻譯，待驗收 |
| Ch13 | Mounted Patrol Operations → `TC_3-21.76_Ch13_車載巡邏_zh-TW.md` | 281–296 | 已翻譯，待驗收 |
| Ch14 | Aviation → `TC_3-21.76_Ch14_航空_zh-TW.md` | 297–310 | 已翻譯，待驗收 |
| Ch15 | Tactical Combat Casualty Care → `TC_3-21.76_Ch15_戰術戰傷救護_zh-TW.md` | 311–324 | 已翻譯，待驗收 |
| 附錄 A | Resources → `TC_3-21.76_AppA_資源_zh-TW.md` | 325–354 | 已翻譯，待驗收 |
| 附錄 B | Quick Reference Cards → `TC_3-21.76_AppB_速查卡_zh-TW.md` | 355–362 | 已翻譯，待驗收 |
| 書末 | Glossary（詞彙表）→ `TC_3-21.76_詞彙表_zh-TW.md` | 365–368 | 已翻譯，待驗收 |
| 彙整 | 全書術語總表（譯稿自製，非原文章節）→ `TC_3-21.76_全書術語總表_zh-TW.md` | — | 793 條，由 `tools/gen_glossary.py` 產生 |
| 書末 | Source Notes／References／Index | 363–364、369–380 | **不翻譯**（保留英文原文） |

> **TC 3-21.76 專屬規則：**
> - **Ch05 爆破**：章節結構、術語、安全注意事項、概念說明照常翻譯；裝藥量公式、起爆系統組裝步驟、爆破操作程序改寫成摘要，並標註原文頁碼供對照。
> - **Ch15 TCCC**：術語沿用 ATP 4-02.11 已拍板的譯法（見 `DEVLOG.md` 2026-08-28 設計師決策 1）。
> - **跨文件術語總表（2026-09-18）**：`術語總表_zh-TW.md`（repo 根目錄）彙整 TC 3-21.76 與 ATP 4-02.11 兩份譯稿的章末術語表，共 1,238 條；TC 單一文件版 793 條於 `TC_3-21.76/`。兩份均由 `tools/gen_glossary.py` 產生（`python3 tools/gen_glossary.py`）。**章末術語表為主檔、總表為產生結果**；改譯名先改章末表再重新產生總表。
> - **章末術語表格式（2026-09-18）**：欄位為 `| 原文 | 譯文 | 說明 |`。說明欄只填「使用者指定或修正過的術語」與譯名易誤解者，其餘留空；外部連結另行統一處理，翻譯階段先不加。
> - **職稱與編組（使用者指定）**：platoon sergeant＝**排士官長**、team leader＝**伍長**、fire team＝**火力伍**、medic＝**醫務兵**、range card＝**射界卡**；cloverleaf method＝**四葉草環繞法**；slough＝**盲汊**；long count／short count＝**單人報數／雙人報數**；combat lifesaver (CLS)＝**戰鬥救護員**（階層低於 CMC＝combat medic＝醫務兵；ATP 4-02.11 共 13 處已於 2026-09-18 一併改為此譯名）；machine gun team＝**機槍組**、aid and litter team＝**救護擔架組**（team 只有指步兵火力伍時才譯「伍」）。其餘術語見各章末術語表。

原始 PDF：`TC_3-21.76/TC_3-21.76_Ranger_Handbook_September_2025.pdf`

---

## 檔案與命名慣例

**現況（P2 架站後，canonical 位置）：**
- 逐章譯文：`docs/atp-4-02.11/<slug>.md`，slug 見〈發佈架構〉對照表；每檔含 frontmatter（`title` / `order` / `status`）
- 圖檔：`docs/public/images/atp-4-02.11/`，命名 `fig-<章2位>-<序2位>.png`（附錄用 `fig-a-01.png`／`fig-b-01.png`）；Markdown 內 `src` 用絕對路徑 `/images/atp-4-02.11/…`（**不加** `base` 前綴）
- 原文勘誤：`docs/errata.md`
- 原始 PDF：續留 `ATP_4-02.11/`，**不進 `docs/`**（不打包進網站）
- 章名中文取原書章標題的通用譯法，跨章保持一致
- slug 以數字前綴排序，`app-a`／`app-b` 自然排在 `20` 之後

> 舊的 `ATP_4-02.11/*_Ch*_zh-TW.md` 檔名已於第七場搬檔時淘汰，不再使用。

---

## 翻譯規則

1. **忠實原文**：不增刪內容、不改寫語氣、不加入原文沒有的臨床建議。
2. **軍語與術語**：TCCC、MARCH、TQ、NPA 等縮寫保留英文，首次出現時括號註中文全稱。已拍板的譯法（見 `DEVLOG.md` 2026-08-28 設計師決策 1，例：`Soldier`＝官兵、`Service member`＝服役人員）所有文件共用。
3. **藥名、劑量、單位**：
   - **藥名與藥品劑量**：完全照原文，**不做任何換算**（例：`acetaminophen 500 mg × 2`）。
   - **英制單位**（長度、距離、重量、溫度等）：保留原數值，括號內加註公制換算，例：「2 英寸（約 5 公分）」「華氏 104 度（攝氏 40 度）」。譯註區塊須註明「實際操作請以原文數值為準」。
4. **結構對齊**：保留原書的標題階層、編號、表格。警告框（WARNING / CAUTION / NOTE）——兩份手冊皆已併入 `docs/`，統一為 VitePress container：WARNING／DANGER → `::: danger`、CAUTION／IMPORTANT → `::: warning`；零星的 `> **註**：…`（NOTE）維持 blockquote。
5. **圖片**：原圖保留英文不重繪，圖下補中文圖說，並標注原書頁碼。兩份手冊（ATP 4-02.11、TC 3-21.76）皆已完成抽圖並併入網站，一律使用 `<figure>` 區塊，`<figcaption>` 依序放中文圖說、原書頁碼、原文圖說：

   ```html
   <figure>
     <img src="<路徑>/fig-06-01.png" alt="圖 6-1．附閥式胸封貼範例" />
     <figcaption>圖 6-1．附閥式胸封貼範例（原書 p.74）<br />原文圖說：Figure 6-1. Vented chest seal examples</figcaption>
   </figure>
   ```

   - `alt` 與 `<figcaption>` 的中文圖說必須一致
   - `src` 用絕對路徑 `/images/<手冊代號>/…`，**不加** `base` 前綴（VitePress 規則）
   - **抽圖流程**（新增手冊時比照辦理）：以 PyMuPDF 依版面座標找出圖片 bbox 並重新渲染（200 dpi PNG），再把佔位改為上述 `<figure>` 格式＋原書頁碼
6. **不確定處**：術語或語意有疑義時停下來問使用者，不自行假設。

---

## 發佈架構（VitePress，2026-08-29 定案）

比照 [`/Projects/tccc-notes/`](../tccc-notes/)：VitePress 1.6 + IBM Carbon 主題 + local 中文搜尋 + GitHub Actions 部署到 Pages。**直接沿用該專案的 `docs/.vitepress/theme/custom.css`。**

### 目錄

```
docs/
├─ index.md                        首頁：hero + 22 張章節卡片 + 版本免責橫幅
├─ atp-4-02.11/<slug>.md           逐章譯文（canonical）
├─ public/images/atp-4-02.11/      圖檔
└─ .vitepress/
   ├─ config.ts                    lang zh-TW、base、側欄（20 章＋附錄 A/B）、local search
   └─ theme/{index.ts,custom.css}
```

### 章節 slug 對照表

| # | 現檔名（`ATP_4-02.11/`） | 架站後（`docs/atp-4-02.11/`） |
|---|---|---|
| 01 | `..._Ch01_傷患處置_zh-TW.md` | `01-casualty-response.md` |
| 02 | `..._Ch02_傷患脫離與搬運_zh-TW.md` | `02-extraction-movement.md` |
| 03 | `..._Ch03_TCCC基礎_zh-TW.md` | `03-tccc-fundamentals.md` |
| 04 | `..._Ch04_大量出血控制_zh-TW.md` | `04-massive-bleeding.md` |
| 05 | `..._Ch05_呼吸道控制_zh-TW.md` | `05-airway.md` |
| 06 | `..._Ch06_呼吸與換氣控制_zh-TW.md` | `06-respiration-ventilation.md` |
| 07 | `..._Ch07_循環控制_zh-TW.md` | `07-circulation.md` |
| 08 | `..._Ch08_低體溫控制_zh-TW.md` | `08-hypothermia.md` |
| 09 | `..._Ch09_二次傷勢評估_zh-TW.md` | `09-secondary-assessment.md` |
| 10 | `..._Ch10_眼部創傷_zh-TW.md` | `10-eye-trauma.md` |
| 11 | `..._Ch11_頭部傷勢_zh-TW.md` | `11-head-injury.md` |
| 12 | `..._Ch12_燒傷_zh-TW.md` | `12-burns.md` |
| 13 | `..._Ch13_骨折與固定_zh-TW.md` | `13-fractures-splinting.md` |
| 14 | `..._Ch14_其他二次傷勢的應急技術_zh-TW.md` | `14-other-field-techniques.md` |
| 15 | `..._Ch15_傷患監測與後送準備_zh-TW.md` | `15-monitoring-evac-prep.md` |
| 16 | `..._Ch16_叮咬與螫傷_zh-TW.md` | `16-bites-stings.md` |
| 17 | `..._Ch17_氣候與環境傷害_zh-TW.md` | `17-environmental-injuries.md` |
| 18 | `..._Ch18_鐮刀型血球特徵_zh-TW.md` | `18-sickle-cell-trait.md` |
| 19 | `..._Ch19_CBRN環境急救_zh-TW.md` | `19-cbrn-first-aid.md` |
| 20 | `..._Ch20_戰鬥與作戰壓力控制_zh-TW.md` | `20-combat-operational-stress.md` |
| A | `..._App-A_急救包與核定醫材清單_zh-TW.md` | `app-a-aid-kits-amal.md` |
| B | `..._App-B_救援裝備_zh-TW.md` | `app-b-rescue-equipment.md` |

### 架站時要做的轉換（P2）

- 搬檔改 slug；每章補 frontmatter（`title` / `order` / `status`）
- 警告框 `> **WARNING / CAUTION / NOTE**` → VitePress container：`::: danger` / `::: warning` / `::: info`
- 來源標頭、譯註區塊保留，樣式交給主題
- `config.ts` 側欄依原書順序（章在前、附錄在後）；`base` 設為 `/notesforselftraining/`
- 圖片路徑一律絕對路徑 `/images/atp-4-02.11/…`，**不加** `base` 前綴（VitePress 規則）

### 加值項目（使用者已同意，全做）

- **原書頁碼錨點**：每章／每圖標「（原書 p.XX）」，做成可對照實體手冊的標記
- **列印／PDF 樣式**：`custom.css` 加 `@media print`，讓整站可列印成離線版
- **版本免責橫幅**：首頁顯示「譯自 ATP 4-02.11，2026 年 3 月版；僅供訓練參考，實際操作以原文為準」
- **來源授權註記**：ATP 為美軍公開刊物（U.S. Government work，公有領域），footer 標明出處即可

---

## 圖片處理工序規格（P1，✅ 2026-08-29 已完成）

> **已執行完畢**，本節保留作為方法紀錄。實際產出與規格的兩處差異見 DEVLOG 第六場：
> ①`src` 過渡期用相對路徑（使用者對話中裁示，架站時再轉絕對路徑）；
> ②附錄 B 的印刷頁偏移為 PDF−13（非全書的 −14），已依原文自身交叉引用校正。

**任務邊界：只做圖片。** 不搬 `.md`、不改 `.md` 檔名、不建 VitePress、不動 `config.ts`。做完更新 DEVLOG ＋本檔進度，交還使用者驗收。

### 1. 抽圖

- 來源：`ATP_4-02.11/ATP_4-02.11_Casualty_Response_TCCC_and_First_Aid_March_2026.pdf`
- 方法：PyMuPDF 依版面座標重新渲染，200 dpi，輸出 PNG（沿用 DEVLOG 2026-08-28 場次選定的「方案 B」）
- 輸出目錄：`docs/public/images/atp-4-02.11/`（不存在就建；這是圖片 canonical 位置，先建好等架站）
- 命名：`fig-<章>-<序>.png`
  - 章：兩位數（`01`…`20`）；附錄用 `a`、`b`
  - 序：兩位數，每章／附錄從 `01` 起，依原書圖號順序
  - 例：`fig-06-01.png`、`fig-13-04.png`、`fig-a-02.png`
- `_圖片測試/` 為舊測試檔，勿沿用其頁碼式命名；本工序完成後可刪

### 2. 佔位替換

全書 15 個檔、共 109 處佔位，格式固定：

```
> **［圖 6-1．附閥式胸封貼範例］**　原文圖說：Figure 6-1. Vented chest seal examples
```

一律替換為：

```
<figure>
  <img src="/images/atp-4-02.11/fig-06-01.png" alt="圖 6-1．附閥式胸封貼範例" />
  <figcaption>圖 6-1．附閥式胸封貼範例（原書 p.74）<br />原文圖說：Figure 6-1. Vented chest seal examples</figcaption>
</figure>
```

- 圖號 `圖 6-1` → 檔名 `fig-06-01`（章號補零）
- `（原書 p.XX）` 填該圖對應的**印刷頁碼**（非 PDF 頁碼）。換算基準：印刷頁 ＝ PDF 頁 − 14（見 Ch04 標頭）；抽圖時逐張核對，書前頁（羅馬數字頁）區段可能不同步
- `src` 用絕對路徑 `/images/…`，**不加** `base` 前綴
- 圖說若含英制度量單位，比照〈翻譯規則第 3 點〉加註公制
- 章末敘述句（如「原文含圖 6-1 至 6-5 共 5 張，本 Markdown 版以標註方式保留圖片位置」）：改為「原文含圖 6-1 至 6-5 共 5 張」，刪掉「以標註方式保留」字樣

### 3. 驗收

- `grep -rn '［圖' ATP_4-02.11/*.md` 結果為 0（全形括號佔位清空）
- `docs/public/images/atp-4-02.11/` 圖片數 ＝ 佔位替換數；每張圖被引用、每個引用有對應圖檔
- 隨機抽 5 章目視確認圖片內容與圖說相符
- 更新 DEVLOG（新場次）與本檔〈目前進度〉

---

## Agent 工作規則

- 執行任何 git 指令前先 `pwd` 確認在本資料夾，`git remote -v` 尾段必須是 `notesforselftraining.git`。
- 一次處理一章，翻完等使用者驗收再繼續下一章。
- 一次只推進一個階段（翻譯／圖片工序／架站／驗收），做完等使用者驗收再進下一階段。
- 網站相關工作比照 [`/Projects/tccc-notes/`](../tccc-notes/) 與 `deploy-to-github-pages` skill。
- 每次收工前更新本檔的「目前進度」表，或寫入 `DEVLOG.md`。
- 不修改父層 `/Projects/` 的制度檔與 skill。
