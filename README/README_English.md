- [切换语言: 简体中文](/README.md) | - [切換語言: 繁體中文](/README/README_繁体中文.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [言語を切り替える: 日本語](/README/README_日本語.md)

# 🤖 Automatic README Generation and Translation Tool

Welcome to the **README-Automatic-Generation-and-Translation-Tool** project! 🎉 This project aims to streamline the generation and translation of your GitHub project documentation, making your README files more professional and multilingual. No matter where you are, you can easily attract more developers! 🌍✨

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
├── README.md          # Main README file for the project
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
├── requirements.txt   # Required dependencies for the project
│
└── tool.py            # Main script for automatic README generation and translation
```

## 📜 License Overview

Our project uses the **Apache License 2.0**, which means you are free to use, modify, and distribute our code, but you must retain the original license and related notices. 📝 Let’s work together to promote open-source collaboration! 💪

## ⚙️ Configuration File

`config.json` is the configuration hub for your project. It allows you to set relevant parameters, such as the repository name, owner information, and supported translation languages (Simplified Chinese, Traditional Chinese, English, Spanish, French, German, Japanese), making it easy for you to switch and manage multilingual content. 🌐💻

## 📦 Dependencies

Our project relies on the following libraries to ensure you can easily set up your development environment:

1. **requests** - A simple HTTP library.
2. **openai** - A library for interacting with the OpenAI API.
3. **GitPython** - A library for operating Git repositories in Python.

You just need to run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

## ⚙️ Feature Overview

The script `tool.py` offers powerful functionality, including:

1. **Configuration Loading** - Reads project parameters from the configuration file.
2. **Repository Interaction** - Retrieves repository files and their contents via the GitHub API.
3. **Content Summarization** - Uses the OpenAI API to summarize repository file contents, generating concise descriptions.
4. **README Generation** - Creates a professional README file based on file structure and summary information.
5. **Translation** - Translates README content into multiple languages while retaining engaging emojis and styles. 😄🎨
6. **Git Operations** - Commits the updated README and translation files to the repository.

## 🚀 Start Your Journey

Just manually trigger the GitHub Actions workflow and wait for a few minutes; the excellent README file will be automatically generated and translated for you to enjoy. ✨

### 🌟 Come and star us! Your support is our motivation to keep moving forward! 💖

Thank you for your attention and support! If you have any questions or suggestions, feel free to contact us on GitHub. We look forward to creating a better open-source community together with you! 🤝