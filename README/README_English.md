- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# README - Automatic Generation and Translation Tool 🌟

Welcome to the **README-Automatic-Generation-and-Translation-Tool** project! 🚀

We are dedicated to providing developers with an automated tool to easily generate and translate README files for GitHub projects, making your project documentation more attractive and professional! 💕

## Project Structure 📂

Here is the current structure of the project, with descriptions of the different files as follows:

```
├── .github
│   └── workflows
│       └── main.yml     # GitHub Actions workflow configuration file
├── LICENSE                # Project license file
├── README.md              # Main documentation of the project
├── README
│   ├── README_Deutsch.md  # German README file
│   ├── README_English.md  # English README file
│   ├── README_Español.md  # Spanish README file
│   ├── README_Français.md # French README file
│   ├── README_日本語.md    # Japanese README file
│   └── README_繁体中文.md   # Traditional Chinese README file
├── config.json            # Project configuration file
├── requirements.txt       # List of Python dependencies
└── tool.py                # Script for auto-generating and updating README files
```

## File Summary 📄

### 1. `.github/workflows/main.yml`
This GitHub Actions workflow configuration file helps us automate the generating and translating of README files. It runs in the latest version of the Ubuntu environment and performs the following steps:

- **Code Checkout**: Fetch the latest code.
- **Set Up Python**: Configure Python 3.8 as the environment.
- **Install Dependencies**: Upgrade pip and install necessary Python packages (requests, openai, GitPython).
- **Run Script**: Execute the Python script (tool.py) using GitHub and OpenAI API credentials to generate the README.

### 2. `LICENSE`
This file contains the Apache License Version 2.0, outlining the terms and conditions for using, copying, and distributing the software and other works. The license provides a legal framework to facilitate open source software development, protecting the rights of contributors and users.

### 3. `config.json`
This configuration file defines important parameters for the project, such as: repository name, owner, base API URL, and default branch (main). It supports the automated generation and translation of README files.

### 4. `requirements.txt`
This lists the dependencies required for the Python project, including:

- **requests**: A popular library that simplifies HTTP requests.
- **openai**: A library for interacting with the OpenAI API.
- **GitPython**: A library for working with and interacting with Git repositories directly from Python.

### 5. `tool.py`
This script automates the generation and updating of README files and their translations in the GitHub repository. Its key functionalities include:

1. **Configuration and Setup**: Loads configuration and retrieves necessary environment variables.
2. **File Management**: Accesses the GitHub repository to get file structure and content.
3. **README Generation**: Utilizes the OpenAI API to generate detailed README files.
4. **Translation Creation**: Translates the generated README into multiple languages.
5. **Link and Structure Integration**: Enhances navigability.
6. **Commit and Push**: Submits the updated files to the GitHub repository.

## Quick Start 🚀

Want to get involved? Click ⭐ in the top right corner to give our project a thumbs up! 💖

With this tool, we help every developer easily maintain project documentation, enhancing the internationalization level of projects! Whether your project is big or small, we can save you the hassle when it comes to documentation, working together to build a better open source ecosystem! 🌍👩‍💻👨‍💻

If you have any questions or suggestions, please feel free to reach out! Happy coding! 🎉