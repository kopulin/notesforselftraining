import { defineConfig } from 'vitepress'

const ATP = '/atp-4-02.11/'
const TC = '/ranger-handbook/'

const atpSidebar = [
  {
    text: 'PART ONE — 傷患處置',
    collapsed: false,
    items: [
      { text: '01｜傷患處置', link: `${ATP}01-casualty-response` },
      { text: '02｜傷患脫離與搬運', link: `${ATP}02-extraction-movement` }
    ]
  },
  {
    text: 'PART TWO — 戰術戰傷救護',
    collapsed: false,
    items: [
      { text: '03｜戰術戰傷救護基礎', link: `${ATP}03-tccc-fundamentals` },
      { text: '04｜大量出血控制（M）', link: `${ATP}04-massive-bleeding` },
      { text: '05｜呼吸道控制（A）', link: `${ATP}05-airway` },
      { text: '06｜呼吸與換氣控制（R）', link: `${ATP}06-respiration-ventilation` },
      { text: '07｜循環控制（C）', link: `${ATP}07-circulation` },
      { text: '08｜低體溫控制（H）', link: `${ATP}08-hypothermia` },
      { text: '09｜二次傷勢評估', link: `${ATP}09-secondary-assessment` },
      { text: '10｜眼部創傷', link: `${ATP}10-eye-trauma` },
      { text: '11｜頭部傷勢', link: `${ATP}11-head-injury` },
      { text: '12｜燒傷', link: `${ATP}12-burns` },
      { text: '13｜骨折與固定', link: `${ATP}13-fractures-splinting` },
      { text: '14｜其他二次傷勢的應急技術', link: `${ATP}14-other-field-techniques` },
      { text: '15｜傷患監測與後送準備', link: `${ATP}15-monitoring-evac-prep` }
    ]
  },
  {
    text: 'PART THREE — 特定傷病照護',
    collapsed: false,
    items: [
      { text: '16｜叮咬與螫傷', link: `${ATP}16-bites-stings` },
      { text: '17｜氣候與環境傷害', link: `${ATP}17-environmental-injuries` },
      { text: '18｜鐮刀型血球特徵', link: `${ATP}18-sickle-cell-trait` },
      { text: '19｜CBRN 環境急救', link: `${ATP}19-cbrn-first-aid` },
      { text: '20｜戰鬥與作戰壓力控制', link: `${ATP}20-combat-operational-stress` }
    ]
  },
  {
    text: '附錄',
    collapsed: false,
    items: [
      { text: 'A｜急救包與核定醫材清單', link: `${ATP}app-a-aid-kits-amal` },
      { text: 'B｜救援裝備', link: `${ATP}app-b-rescue-equipment` }
    ]
  },
  {
    text: '其他',
    collapsed: false,
    items: [
      { text: '原文勘誤彙整', link: '/errata' }
    ]
  }
]

const tcSidebar = [
  {
    text: '書前',
    collapsed: false,
    items: [
      { text: '前言與導言', link: `${TC}00-preface-introduction` }
    ]
  },
  {
    text: '正文',
    collapsed: false,
    items: [
      { text: '01｜領導', link: `${TC}01-leadership` },
      { text: '02｜作戰', link: `${TC}02-operations` },
      { text: '03｜火力支援', link: `${TC}03-fire-support` },
      { text: '04｜通訊', link: `${TC}04-communications` },
      { text: '05｜爆破', link: `${TC}05-demolitions` },
      { text: '06｜行進', link: `${TC}06-movement` },
      { text: '07｜巡邏', link: `${TC}07-patrols` },
      { text: '08｜戰鬥演練', link: `${TC}08-battle-drills` },
      { text: '09｜軍事登山', link: `${TC}09-military-mountaineering` },
      { text: '10｜機槍運用', link: `${TC}10-machine-gun-employment` },
      { text: '11｜城鎮作戰', link: `${TC}11-urban-operations` },
      { text: '12｜水上作戰', link: `${TC}12-waterborne-operations` },
      { text: '13｜車載巡邏', link: `${TC}13-mounted-patrol-operations` },
      { text: '14｜航空', link: `${TC}14-aviation` },
      { text: '15｜戰術戰傷救護', link: `${TC}15-tactical-combat-casualty-care` }
    ]
  },
  {
    text: '附錄',
    collapsed: false,
    items: [
      { text: 'A｜資源', link: `${TC}app-a-resources` },
      { text: 'B｜速查卡', link: `${TC}app-b-quick-reference-cards` }
    ]
  },
  {
    text: '其他',
    collapsed: false,
    items: [
      { text: '詞彙表（Glossary）', link: `${TC}glossary` }
    ]
  }
]

export default defineConfig({
  lang: 'zh-TW',
  title: '手冊中文譯本',
  description:
    '美軍準則手冊逐章繁體中文翻譯（ATP 4-02.11、TC 3-21.76），僅供訓練參考。',

  base: '/notesforselftraining/',
  cleanUrls: true,
  lastUpdated: true,

  head: [
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', {
      href: 'https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@300;400;600&family=IBM+Plex+Mono:wght@400;600&display=swap',
      rel: 'stylesheet'
    }]
  ],

  themeConfig: {
    siteTitle: '手冊中文譯本',
    nav: [
      { text: '首頁', link: '/' },
      { text: 'Casualty Response', link: ATP },
      { text: 'Ranger Handbook', link: TC },
      { text: 'ATP 原文勘誤', link: '/errata' }
    ],

    sidebar: {
      [ATP]: atpSidebar,
      '/errata': atpSidebar,
      [TC]: tcSidebar
    },

    search: {
      provider: 'local',
      options: {
        locales: {
          root: {
            translations: {
              button: { buttonText: '搜尋', buttonAriaLabel: '搜尋' },
              modal: {
                displayDetails: '顯示詳情',
                noResultsText: '找不到相關內容',
                resetButtonTitle: '清除查詢',
                footer: { selectText: '選擇', navigateText: '切換', closeText: '關閉' }
              }
            }
          }
        }
      }
    },

    outline: { label: '本頁目錄', level: [2, 3] },
    docFooter: { prev: '上一章', next: '下一章' },
    darkModeSwitchLabel: '深色模式',
    lightModeSwitchTitle: '切換至淺色模式',
    darkModeSwitchTitle: '切換至深色模式',
    returnToTopLabel: '回到頂部',
    sidebarMenuLabel: '選單',
    lastUpdatedText: '最後更新',

    footer: {
      message:
        '原文為美國聯邦政府公開刊物（ATP 4-02.11、TC 3-21.76，U.S. Government work，公有領域）。本站僅提供非官方繁體中文翻譯，僅供訓練參考，實際操作一律以英文原文為準。',
      copyright: '譯文 © 2026 kopulin｜依原文授權以公有領域方式釋出'
    }
  },

  markdown: {
    lineNumbers: false
  }
})
