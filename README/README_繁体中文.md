- [切换语言: 简体中文](/README.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# README - 自動化生成與翻譯工具 🌟

歡迎來到 **README-Automatic-Generation-and-Translation-Tool** 專案！🚀

我們致力於為開發者提供一個自動化工具，以輕鬆生成和翻譯GitHub專案的README文件，讓你的專案文檔更具吸引力和專業感！💕 

## 專案結構 📂

以下是當前專案的結構，對於不同文件的說明如下：

```
├── .github
│   └── workflows
│       └── main.yml     # GitHub Actions工作流配置文件
├── LICENSE                # 專案許可證文件
├── README.md              # 專案的主要文檔
├── README
│   ├── README_Deutsch.md  # 德語README文件
│   ├── README_English.md  # 英語README文件
│   ├── README_Español.md  # 西班牙語README文件
│   ├── README_Français.md # 法語README文件
│   ├── README_日本語.md    # 日語README文件
│   └── README_繁體中文.md   # 繁體中文README文件
├── config.json            # 專案配置文件
├── requirements.txt       # Python依賴庫列表
└── tool.py                # 自動生成和更新README文件的腳本
```

## 文件摘要 📄

### 1. `.github/workflows/main.yml`
這個GitHub Actions工作流配置文件幫助我們實現了README文件的生成和翻譯自動化。它在最新版本的Ubuntu環境中運行，執行以下步驟：

- **代碼檢出**：獲取最新的代碼。
- **設置Python**：配置Python 3.8作為環境。
- **安裝依賴**：升級pip並安裝所需的Python包（requests、openai、GitPython）。
- **運行腳本**：執行Python腳本（tool.py），使用GitHub和OpenAI API憑據生成README。

### 2. `LICENSE`
該文件包含Apache許可證版本2.0，概述了使用、複製和分發軟體和其他作品的條款與條件。許可證提供了法律框架，促進開源軟體開發，保護貢獻者和用戶的權益。

### 3. `config.json`
這個配置文件定義了專案的重要參數，如：倉庫名稱、擁有者、基本API URL和默認分支（main）。它支持自動生成和翻譯README文件。

### 4. `requirements.txt`
列出了Python專案所需的依賴庫，包括：

- **requests**：簡化HTTP請求的流行庫。
- **openai**：與OpenAI API互動的庫。
- **GitPython**：直接從Python操作和互動Git倉庫的庫。

### 5. `tool.py`
這個腳本自動化生成和更新GitHub倉庫中的README文件及其翻譯。其關鍵功能包括：

1. **配置與設置**：加載配置，獲取必要的環境變量。
2. **文件管理**：訪問GitHub倉庫，獲取文件結構和內容。
3. **README生成**：利用OpenAI的API生成詳細的README文件。
4. **翻譯創建**：將生成的README翻譯成多種語言。
5. **鏈接與結構集成**：增強可導航性。
6. **提交與推送**：將更新後的文件提交到GitHub倉庫。

## 快速開始 🚀

想要參與嗎？點擊右上角的⭐贊一下我們的專案吧！ 💖 

透過這個工具，我們幫助每個開發者都能輕鬆維護專案文檔，提升專案的國際化水平！無論你的專案是大還是小，我們都能讓你在文檔方面省去煩惱，共同打造一個更好的開源生態！🌍👩‍💻👨‍💻

如果你有任何問題或建議，請隨時與我們聯繫！happy coding！🎉