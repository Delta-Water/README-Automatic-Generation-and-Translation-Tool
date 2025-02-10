[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) | [Español](/README/README_es.md) | [Français](/README/README_fr.md) | [Deutsch](/README/README_de.md) | [日本語](/README/README_ja.md)

- [Switch Language: Traditional Chinese](/README/README_繁体中文.md) | - [切換語言: 英語](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Automatic Generation and Translation README Tool

Welcome to the **README-Automatic-Generation-and-Translation-Tool** project! 🎉 This project aims to simplify the generation and translation of your GitHub project documentation, making your README file more professional and multilingual. No matter where you are, you can easily attract more developers! 🌍✨

## 🚀 Project Structure

Here’s an overview of the project structure:

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # GitHub Actions workflow file
│
├── LICENSE            # Apache License 2.0
│
├── README.md          # The main README file for the project
│
├── README/
│   ├── README_Deutsch.md     # German README 
│   ├── README_English.md      # English README 
│   ├── README_Español.md      # Spanish README 
│   ├── README_Français.md     # French README 
│   ├── README_日本語.md        # Japanese README 
│   └── README_繁体中文.md      # Traditional Chinese README 
│
├── config.json       # Configuration file containing settings and translation languages
│
├── requirements.txt   # Required libraries for the project
│
└── tool.py            # Main script for automatic generation and translation of README
```

## 📜 License Overview

Our project uses the **Apache License 2.0**, which means you can freely use, modify, and distribute our code, as long as you retain the original license and relevant notices. 📝 Let’s promote open-source collaboration together! 💪

## ⚙️ Configuration File

`config.json` is the configuration center for your project. It allows you to set relevant parameters, such as repository name, owner information, and supported translation languages (Simplified Chinese, Traditional Chinese, English, Spanish, French, German, Japanese), allowing you to easily switch and manage multilingual content. 🌐💻

## 📦 Dependencies

Our project relies on the following libraries to ensure you can easily set up the development environment:

1. **requests** - A simple HTTP request library.
2. **openai** - A library for interacting with the OpenAI API.
3. **GitPython** - A library for operating Git repositories through Python.

You just need to run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

## ⚙️ Feature Overview

The script `tool.py` offers powerful features, including:

1. **Configuration Loading** - Reads project parameters from the configuration file.
2. **Repository Interaction** - Retrieves repository files and content through the GitHub API.
3. **Content Summarization** - Uses the OpenAI API to summarize repository file content, generating concise descriptions.
4. **README Generation** - Generates a professional README file based on file structure and summary information.
5. **Translation** - Translates README content into multiple languages, retaining lively emojis and styles. 😄🎨
6. **Git Operations** - Commits the updated README and translation files to the repository.

## 🚀 Start Your Journey

Simply manually trigger the GitHub Actions workflow, wait a few minutes, and a wonderful README file will be automatically generated and translated for you to enjoy. ✨

### 🌟 Come and star us! Your support is our motivation to keep moving forward! 💖

Thank you for your attention and support! If you have any questions or suggestions, please feel free to contact us on GitHub. We look forward to creating a better open-source community together with you! 🤝