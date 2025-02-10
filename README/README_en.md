<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Automated README Generation and Translation Tool

Welcome to the world of the **Automated README Generation and Translation Tool**! 🎉 This project aims to provide developers and project maintainers with an efficient and convenient solution to easily generate, optimize, and translate README files, delivering professional and engaging documentation for your code. Whether you are a beginner or an experienced developer, the tools you need are right here! 🌟

## 🛠️ Project Structure

Here is the basic structure of the project, clear and easy to use:

```
.
├── .github
│   └── workflows
│       ├── generate.yml      # Workflow for automatically generating README files
│       ├── optimize.yml      # Workflow for optimizing README files
│       └── translate.yml      # Workflow for translating README files
├── LICENSE                   # Project license
├── README.md                 # Project description file
├── config.json               # Tool configuration file
├── requirements.txt          # List of dependencies
└── tool.py                   # Automation script
```

## ✨ Core Features

1. **Automated README Generation**: Use GitHub Actions workflows to automatically generate professional README files from project code.
2. **Optimization Feature**: Implement AI-driven optimization through OpenAI’s API to enhance the quality of existing README documentation.
3. **Translation Capabilities**: Automatically translate the README file into multiple languages, making your project easily accessible to a broader audience. 👌

## ⚙️ Workflows

### 1. `generate.yml`
- Manually triggered via `workflow_dispatch` to generate README files.
- Runs in an Ubuntu environment, installing necessary dependencies (`requests`, `openai`, `GitPython`).
- Finally executes the `tool.py generate` script to create a professional README.

### 2. `optimize.yml`
- Manually triggered to automatically optimize existing README files.
- Includes steps for code checks, Python environment setup, and dependency installation.
- Executes the `tool.py optimize` script to improve README readability.

### 3. `translate.yml`
- Manually triggered to automatically translate README files.
- After checking out the code, setting up the Python environment, and installing necessary dependencies, it runs the translation script.

## 📝 Configuration Instructions

The `config.json` file contains the tool’s basic configurations and options, including:
- Repository name and owner
- Base URL for the API and the language model used
- Languages to be translated and their abbreviations
- ...

Please ensure this file is configured correctly for the tool to function properly. 🔑

## 📦 Dependencies

You can find the required dependencies for the project in `requirements.txt`:
- **requests**: A user-friendly HTTP request library.
- **openai**: A library for interacting with the OpenAI API.
- **GitPython**: A Python library for interacting with Git repositories.

Make sure to install these dependencies for the project to run smoothly! 🚀

## 🖥️ Key Features Overview

The `tool.py` script is the core of this project and provides the following functionalities:
- Automatically loads the configuration file and manages project settings.
- Interactively retrieves repository files and generates summaries.
- Creates, optimizes, and translates README files, committing changes via Git.

You can also flexibly execute specific commands through the command-line interface to meet different needs! 🎈

## 🌸 How to Use?

You can choose to fork this project, utilize `GitHub Actions`, or clone it locally. Here’s an example using `GitHub Actions`:

1. Add `PAT` and `OPENAI_API_KEY` to the secrets.
2. Configure necessary parameters in the `config.json` file.
3. Manually trigger the workflow you wish to execute.

Please note that `optimize.yml` and `translate.yml` require an existing README file in the target repository to execute.

## 📜 License

This project is licensed under the **Apache License 2.0**, see the `LICENSE` file for more details.

## 🤝 Contributions and Support

We warmly welcome your contributions! If you find this tool helpful, please give us a ⭐️. Your support is the motivation that drives us forward! 💪

---

With this tool, you can easily create professional and readable documentation. Give it a try—saving time and effort, this project is worth bookmarking! 🌟