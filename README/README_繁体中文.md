- [切换语言: 简体中文](/README.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# 自動生成與翻譯 README 工具 🛠️✨

歡迎使用 **自動生成與翻譯 README 工具** 項目！本工具旨在簡化和提升 GitHub 存儲庫中 README 文件的管理與翻譯，無論您是項目維護者還是新用戶，都能使您的工作流程變得更加高效和愉快！😄

## 項目結構 🗂️

以下是目錄結構，幫助您快速了解每個文件和文件夾的用途：

```
.github
└── workflows
    ├── generate.yml         # 自動生成 README 文件的工作流
    ├── optimize.yml         # 自動優化 README 文件的工作流
    └── translate.yml        # 自動翻譯 README 文件的工作流

LICENSE                        # 項目許可證文件
README.md                     # 項目的主 README 文件
README
├── README_Deutsch.md        # 德語 README
├── README_English.md        # 英語 README
├── README_Español.md       # 西班牙語 README
├── README_Français.md       # 法語 README
├── README_日本語.md         # 日語 README
└── README_繁體中文.md      # 中文（繁體）README

config.json                   # 配置文件
requirements.txt              # Python 依賴文件
tool.py                       # 自動化工具腳本
```

## 工作流概述 🚀

### 1. `generate.yml`
此 GitHub Actions 工作流用於自動生成和更新 README 文件。主要步驟包括：

- 檢出代碼
- 設置 Python 3.8 環境
- 安裝所需依賴（`requests`、`openai`、`GitPython`）
- 運行腳本（`tool.py generate`）生成或更新 README 文件
- 配置 Git 並推送更新的 README 文件

這一過程簡化了 README 文件的維護，讓您能夠專注於更重要的事務！😎

### 2. `optimize.yml`
該工作流自動優化 README 文件，同樣通過 `workflow_dispatch` 事件手動觸發。關鍵步驟包括：

- 檢出代碼
- 設置 Python 3.8 環境
- 安裝依賴
- 運行腳本（`tool.py optimize`）提升 README 內容
- 提交並推送更新的 README 文件

讓我們共同提升內容質量！💪

### 3. `translate.yml`
該工作流自動翻譯 README 文件，確保您的項目能夠接觸到更廣泛的受眾。步驟包括：

- 檢出代碼
- 設置 Python 3.8 環境
- 安裝依賴
- 運行翻譯腳本（`tool.py`）

它是您在多語言時代的終極助手！🌍

## 許可證 📄
本項目遵循 Apache 許可證 2.0，允許您使用、修改和分發代碼，同時保障您的權利與義務。

## 配置管理 🛠️
`config.json` 文件定義了重要設置，如 API 端點和支持的翻譯語言，以確保工具的順利運行並支持多語言功能。🤓

## 依賴管理 🐍
`requirements.txt` 文件列出了必要的 Python 包，包括：

- **requests**：簡化 HTTP 請求
- **openai**：訪問 OpenAI API 進行各種操作
- **GitPython**：在 Python 中與 Git 存儲庫交互

請確保安裝這些依賴，以確保工具的順利運行！🌟

## 如何使用？

您可以選擇 fork 本項目並使用 `GitHub Actions`，或將其克隆到本地使用。

以下是使用 GitHub Actions 的示例：

1. 在 GitHub Secrets 中添加 `PAT` 和 `OPENAI_API_KEY`。
2. 編輯 `config.json` 配置相關參數。
3. 如果希望生成並翻譯 README 文件：
   - 手動運行 `generate` 工作流，這將生成一個 `.README.md` 文件在倉庫根目錄。
   - 審閱和修改該文件後再提交。
   - 手動觸發 `translate` 工作流，工具會將已編輯的 README 添加到目標倉庫並生成翻譯版本。

完成！🎉

如果您已準備好一個 README 文件並希望僅進行翻譯：
- 將其推送到工具倉庫的 `.README.md` 文件中。
- 手動觸發 `translate` 工作流。

完成！🎉

## 反饋與貢獻 🙌
我們歡迎您的反饋和建議！請隨時為這個項目點贊⭐️並參與其中，共同提升項目的質量與可用性。

感謝您的關注與支持！讓我們攜手讓 README 文件更加生動有趣！🎉