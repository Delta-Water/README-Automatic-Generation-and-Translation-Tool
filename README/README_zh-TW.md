<div align="center">

[zh](/README.md) | [English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 自動化 README 生成與翻譯工具

歡迎來到 **README 自動化生成與翻譯工具** 項目！🎉 本項目旨在為開發者和項目維護者提供一個便捷的方式，輕鬆生成、優化和翻譯 README 文件。無論你是新手還是專家，只需簡單幾步，即可獲得一份專業、引人入勝的 README 文件！ 🚀

## 📂 項目結構

```plaintext
./
└── workflows/
│   ├── generate.yml      # 自動生成 README 文件的工作流
│   ├── optimize.yml      # 自動優化 README 文件的工作流
│   └── translate.yml      # 自動翻譯 README 文件的工作流
└── LICENSE                # Apache 許可證文件
└── README.md              # 項目的自述文件
└── config.json            # 配置文件，定義項目參數
└── requirements.txt       # Python 依賴包列表
└── tool.py                # 自動化處理工具
```

## ⚙️ 文件簡介

### `.github/workflows/generate.yml`
該工作流通過 GitHub Actions 進行項目 README 文件的自動生成。手動觸發後，它執行以下步驟：
1. 檢出項目代碼；
2. 設定 Python 3.8 環境；
3. 安裝所需依賴（`requests`、`openai`、`GitPython`）；
4. 執行 `tool.py generate` 腳本生成 README 文件。

### `.github/workflows/optimize.yml`
此工作流用於自動優化 README 文件，手動觸發後，主要執行以下步驟：
1. 檢出代碼；
2. 設定 Python 3.8 環境；
3. 安裝必要依賴；
4. 執行 `tool.py optimize`，通過 OpenAI API 進行優化處理。

### `.github/workflows/translate.yml`
該工作流用於自動翻譯項目的 README 文件，同樣通過手動觸發啟動。步驟包括：
1. 檢出代碼；
2. 設定 Python 3.8 環境；
3. 安裝依賴；
4. 執行 `tool.py translate` 進行翻譯。

### `LICENSE`
此文件包含 Apache 許可證第 2 版，允許用戶在遵守相關條件下，自由使用、修改和分發本項目，以保護原作者和貢獻者的權益。

### `config.json`
此配置文件定義了項目運行所需的各種參數，包括倉庫信息、API 基礎網址、模型及支持的翻譯語言。

### `requirements.txt`
列出項目所需的 Python 包，包括：
- `requests`: 用於處理 HTTP 請求，簡化網絡交互。
- `openai`: 與 OpenAI API 進行交互，實現 AI 模型的調用。
- `GitPython`: 提供對 Git 倉庫的操作支持。

### `tool.py`
核心腳本用於自動化處理 README，主要功能包括：
1. 加載配置；
2. 獲取倉庫內容；
3. 生成 README 內容；
4. 完善和翻譯 README；
5. 提交變更；
6. 提供命令行接口。

## 🌸 如何使用？

你可以選擇 Fork 本項目後使用 `GitHub Actions`，或者將其克隆到本地進行使用。以下將以前者為例，後者請自行配置。

1. 首先，將 `PAT` 和 `OPENAI_API_KEY` 添加到 Secrets 中。
2. 接著，進入 `config.json` 配置相關參數。
3. 如需生成 README，請手動觸發 `generate` 工作流。
4. 如需優化 README，請手動觸發 `optimize` 工作流。
5. 如需翻譯 README，請手動觸發 `translate` 工作流。

## 🌟 讓我們開始吧！

別再猶豫了！使用這個工具提升你的項目文檔質量，吸引更多的協作與關注！如果你覺得這個項目對你有幫助，請給我們一個 💖 Star！讓我們共同努力，讓開源社區更加美好！🌈

## 📄 許可證

本項目採用 Apache 許可證，詳細信息請查看 [LICENSE](LICENSE) 文件。

歡迎加入我們，讓 README 變得更加簡單高效！🚀