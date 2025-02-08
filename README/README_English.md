- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Project Name

Welcome to our project! ✨ This project aims to automatically generate and translate README files, providing comprehensive documentation for your GitHub repository. Now, let’s take a look at the project structure and a detailed introduction to each file!

## Project Structure

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/main.yml": "main.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "config.json": "config.json",
  "requirements.txt": "requirements.txt",
  "tool.py": "tool.py"
}
```

### File Descriptions

#### `.github/workflows/main.yml`
This is the key file that defines the GitHub Actions workflow, named “Automatically Generate and Translate README”. 🔄  
You can trigger this workflow manually using the `workflow_dispatch` event. It includes a task called “build” that runs in an Ubuntu environment. The goal of this workflow is to automate the generation and translation of README files, eliminating the hassle of manual updates.

#### `LICENSE`
This document contains the full text of the Apache License Version 2.0, outlining the terms and conditions for using, copying, and distributing the software and its derivatives. 🛡️  
It grants users broad permissions to modify, use, and distribute works protected by this license, while also stipulating certain obligations. Through this license, we aim to promote open collaboration and the sharing of intellectual property.

#### `README.md`
This is the primary README file for the project, providing users with an overview, usage instructions, and other important information. 📊  
In this document, we summarize all the key information about the project to help users get started quickly!

#### `README` Folder
- `README/README_Deutsch.md`: German translation.
- `README/README_English.md`: English translation.
- `README/README_Español.md`: Spanish translation.
- `README/README_Français.md`: French translation.
- `README/README_日本語.md`: Japanese translation.
- `README/README_繁体中文.md`: Traditional Chinese translation.

This folder contains multilingual versions of the project README, making it easy for global users to understand and utilize the project. 🌍📚

#### `config.json`
This file is the configuration file for the tool that automatically generates and translates README documents. 🔧  
It includes parameters such as the repository name, owner, base URL for API access, the main branch used, and supported translation languages. The configuration aims to streamline the localization and translation process for project documentation.

#### `requirements.txt`
This is a standard list of external libraries required for the Python project, ensuring that the development environment can run the needed dependencies smoothly. 📦  
It includes:
1. **requests**: A library for easy interaction with web services and REST APIs.
2. **openai**: A library that provides access to the OpenAI API, supporting natural language processing and machine learning tasks.
3. **GitPython**: A library that allows users to interact with Git repositories programmatically.

#### `tool.py`
This is a Python script used to automatically generate and update the README file of a GitHub repository. 🤖  
Its main features include:
- Loading configuration parameters.
- Interacting with the GitHub repository to extract file structure and content.
- Using the OpenAI API to generate file summaries.
- Compiling generated summaries and structures to construct a professional README file.
- Translating README content into multiple languages to enhance accessibility.
- Updating the README and translation files and committing changes back to GitHub.

### 📢 Get Started!
If you find this project helpful, please don’t hesitate to give us a ⭐️! Every star is a recognition of our hard work! Thank you for your support as we work together to advance open-source progress! 🚀

---

If you have any questions or suggestions, feel free to reach out to us! We look forward to your valuable feedback! ❤️