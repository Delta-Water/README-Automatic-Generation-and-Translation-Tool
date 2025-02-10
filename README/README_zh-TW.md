<div align="center">

[简体中文](/README.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 自動化 README 生成與翻譯工具

歡迎來到 **自動化 README 生成與翻譯工具** 的世界！🎉 本專案旨在為開發者和專案維護者提供一個高效便捷的解決方案，輕鬆生成、優化和翻譯 README 檔案，為程式碼提供專業且引人入勝的文件。無論您是新手還是經驗豐富的開發者，這裡都有您所需的工具！🌟

## 🛠️ 專案結構

以下是專案的基本結構，一目了然，方便您的使用：

```
.
├── .github
│   └── workflows
│       ├── generate.yml      # 自動生成 README 檔案的工作流程
│       ├── optimize.yml      # 優化 README 檔案的工作流程
│       └── translate.yml      # 翻譯 README 檔案的工作流程
├── LICENSE                   # 專案許可證
├── README.md                 # 專案說明檔
├── config.json               # 工具配置檔
├── requirements.txt          # 依賴庫列表
└── tool.py                   # 自動化腳本
```

## ✨ 核心功能

1. **自動化 README 生成**：借助 GitHub Actions 工作流程，從專案程式碼中自動生成專業的 README 檔案。
2. **優化功能**：通過 OpenAI 的 API，實現 AI 驅動的優化，提升現有 README 文件的質量。
3. **翻譯能力**：自動將 README 檔案翻譯成多種語言，助力更廣泛的受眾輕鬆訪問您的專案👌。

## ⚙️ 工作流程

### 1. `generate.yml`
- 手動觸發，通過 `workflow_dispatch` 生成 README 檔案。
- 在 Ubuntu 環境下運行，安裝所需依賴（`requests`, `openai`, `GitPython`）。
- 最後執行 `tool.py generate` 腳本，生成專業的 README。

### 2. `optimize.yml`
- 手動觸發，自動優化現有 README 檔案。
- 包含代碼檢查、Python 環境設置和依賴安裝的步驟。
- 執行 `tool.py optimize` 腳本，提升 README 的可讀性。

### 3. `translate.yml`
- 手動觸發，自動翻譯 README 檔案。
- 檢出代碼、設置 Python 環境、安裝所需依賴後，運行翻譯腳本。

## 📝 配置說明

`config.json` 檔案包含了工具的基本配置和選項，包括：
- 倉庫名稱和所有者
- API 的基本 URL 和所用語言模型
- 需要翻譯的語言及其縮寫
- …

請確保正確配置此檔案，以確保工具的正常運行。🔑

## 📦 依賴庫

在 `requirements.txt` 中您可以找到專案所需的依賴庫：
- **requests**：用戶友好的 HTTP 請求庫。
- **openai**：與 OpenAI 的 API 互動的庫。
- **GitPython**：用於與 Git 倉庫互動的 Python 庫。

請確保安裝這些依賴，以順利運行專案！🚀

## 🖥️ 關鍵功能詳解

`tool.py` 腳本是本專案的核心，提供了以下功能：
- 自動加載配置檔，管理專案設置。
- 互動式獲取倉庫文件並生成文件摘要。
- 創建、優化和翻譯 README 檔案，並通過 Git 操作進行提交。

您還可以通過命令行界面靈活執行特定命令，以滿足不同需求！🎈

## 🌸 如何使用？

您可以選擇 fork 本專案，使用 `GitHub Actions`，或者克隆到本地使用。以下以使用 `GitHub Actions` 為例：

1. 將 `PAT` 和 `OPENAI_API_KEY` 添加到 secrets。
2. 進入 `config.json` 配置相關參數。
3. 手動觸發想要執行的工作流程即可。

請注意，`optimize.yml` 和 `translate.yml` 需要在目標倉庫中已有 README 檔案才能執行。

## 📜 許可證

本專案遵循 **Apache License 2.0** 許可證，詳見 `LICENSE` 檔案。

## 🤝 貢獻與支持

我們非常歡迎您的貢獻！如果您覺得這個工具對您有幫助，請給我們一個 ⭐️。您的支持是我們不斷前行的動力！💪

---

透過這個工具，您可以輕鬆創建專業、易讀的文檔。快來試試吧，省時省力，這個專案值得您收藏！🌟