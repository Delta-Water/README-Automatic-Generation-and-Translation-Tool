[zh](/README.md) | [English](/README/README_en.md) | [Español](/README/README_es.md) | [Français](/README/README_fr.md) | [Deutsch](/README/README_de.md) | [日本語](/README/README_ja.md)

- [切換語言: 繁體中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 自動生成與翻譯 README 工具

歡迎來到 **README-Automatic-Generation-and-Translation-Tool** 專案！🎉 這個專案旨在簡化您的 GitHub 專案文檔生成與翻譯工作，讓您的 README 文件更加專業和多語言化，無論您身在何處，都能輕鬆吸引更多的開發者！🌍✨

## 🚀 專案結構

以下是專案的結構概覽：

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # GitHub Actions 工作流文件
│
├── LICENSE            # Apache 授權 2.0
│
├── README.md          # 專案的主要 README 文件
│
├── README/
│   ├── README_Deutsch.md     # 德語 README 
│   ├── README_English.md      # 英語 README 
│   ├── README_Español.md      # 西班牙語 README 
│   ├── README_Français.md     # 法語 README 
│   ├── README_日本語.md        # 日語 README 
│   └── README_繁體中文.md      # 繁體中文 README 
│
├── config.json       # 配置文件，包括設定與翻譯語言
│
├── requirements.txt   # 專案所需的依賴庫
│
└── tool.py            # 自動生成與翻譯 README 的主要腳本
```

## 📜 授權概要

我們的專案採用 **Apache 授權 2.0**，這意味著您可以自由使用、修改和分發我們的代碼，但需保留原始授權和相關聲明。📝 讓我們共同促進開源合作吧！💪

## ⚙️ 配置文件

`config.json` 是您專案的配置中心。它允許您設置相關參數，如倉庫名稱、擁有者信息及支持的翻譯語言（簡體中文、繁體中文、英語、西班牙語、法語、德語、日語），讓您能輕鬆切換和管理多語言內容。🌐💻

## 📦 依賴庫

我們的專案依賴以下庫，確保您可以輕鬆搭建開發環境：

1. **requests** - 簡單的HTTP請求庫。
2. **openai** - 與 OpenAI API 互動的庫。
3. **GitPython** - 通過 Python 操作 Git 倉庫的庫。

您只需要運行以下命令安裝依賴：

```bash
pip install -r requirements.txt
```

## ⚙️ 功能概述

腳本 `tool.py` 提供了強大的功能，包括：

1. **配置加載** - 從配置文件中讀取專案參數。
2. **倉庫互動** - 通過 GitHub API 獲取倉庫文件及其內容。
3. **內容摘要** - 利用 OpenAI 的 API 摘要倉庫文件內容，生成簡潔的描述。
4. **README 生成** - 根據文件結構與摘要信息生成專業的 README 文件。
5. **翻譯** - 將 README 內容翻譯成多種語言，保留活潑的表情符號和樣式。😄🎨
6. **Git 操作** - 提交更新後的 README 和翻譯文件到倉庫。

## 🚀 開啟之旅

只需手動啟動 GitHub Actions 工作流，等待幾分鐘，優秀的 README 文件將自動生成並翻譯好，您可以盡情享受這一切的美好。✨

### 🌟 快來為我們加星吧！您的支持是我們不斷前進的動力！💖

感謝您的關注和支持！如有任何問題或建議，請隨時在GitHub上與我們聯繫。我們期待著與您共同創造更美好的開源社區！🤝