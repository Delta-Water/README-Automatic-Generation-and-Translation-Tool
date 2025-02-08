- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Automatic README Generation and Translation Tool

Welcome to the **README-Automatic-Generation-and-Translation-Tool** project! 🎉 This project aims to simplify the generation and translation of your GitHub project documentation, making your README files more professional and multilingual. No matter where you are, you can easily attract more developers! 🌍✨

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
├── README.md          # Main README file of the project
│
├── README/
│   ├── README_Deutsch.md     # German README 
│   ├── README_English.md      # English README 
│   ├── README_Español.md      # Spanish README 
│   ├── README_Français.md     # French README 
│   ├── README_日本語.md        # Japanese README 
│   └── README_繁体中文.md      # Traditional Chinese README 
│
├── config.json       # Configuration file, including settings and translation languages
│
├── requirements.txt   # Required libraries for the project
│
└── tool.py            # Main script for automatic README generation and translation
```

## 📜 License Overview

Our project is licensed under the **Apache License 2.0**, which means you can freely use, modify, and distribute our code, as long as you retain the original license and relevant notices. 📝 Let’s promote open-source collaboration together! 💪

## ⚙️ Configuration File

`config.json` is the configuration center for your project. It allows you to set parameters like repository name, owner information, and supported translation languages (Simplified Chinese, Traditional Chinese, English, Spanish, French, German, Japanese), enabling you to easily switch and manage multilingual content. 🌐💻

## 📦 Dependencies

Our project relies on the following libraries to ensure you can easily set up your development environment:

1. **requests** - A simple HTTP request library.
2. **openai** - A library for interacting with the OpenAI API.
3. **GitPython** - A library for operating Git repositories through Python.

You only need to run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

## ⚙️ Feature Overview

The `tool.py` script offers powerful functionalities, including:

1. **Configuration Loading** - Reads project parameters from the configuration file.
2. **Repository Interaction** - Uses the GitHub API to fetch repository files and their content.
3. **Content Summarization** - Utilizes OpenAI's API to summarize repository file contents and generate concise descriptions.
4. **README Generation** - Creates a professional README file based on the file structure and summary information.
5. **Translation** - Translates README content into multiple languages while keeping lively emojis and styles. 😄🎨
6. **Git Operations** - Commits the updated README and translated files to the repository.

## 🚀 Start Your Journey

Just manually trigger the GitHub Actions workflow, wait a few minutes, and an excellent README file will be automatically generated and translated. You can fully enjoy the beauty of it all. ✨

### 🌟 Please give us a star! Your support is the driving force behind our progress! 💖

Thank you for your attention and support! If you have any questions or suggestions, feel free to contact us on GitHub. We look forward to creating a better open-source community together with you! 🤝