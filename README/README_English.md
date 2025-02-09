- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Automatic README Generation and Translation Tool 🛠️✨

Welcome to the **Automatic README Generation and Translation Tool** project! This tool is designed to simplify and enhance the management and translation of README files in GitHub repositories. Whether you are a project maintainer or a new user, this tool will make your workflow more efficient and enjoyable! 😄

## Project Structure 🗂️

Here’s the directory structure to help you quickly understand the purpose of each file and folder:

```
.github
└── workflows
    ├── generate.yml         # Workflow for automatically generating README files
    ├── optimize.yml         # Workflow for automatically optimizing README files
    └── translate.yml        # Workflow for automatically translating README files

LICENSE                        # Project license file
README.md                     # Main README file for the project
README
├── README_Deutsch.md        # German README
├── README_English.md        # English README
├── README_Español.md        # Spanish README
├── README_Français.md       # French README
├── README_日本語.md         # Japanese README
└── README_繁体中文.md      # Chinese (Traditional) README

config.json                   # Configuration file
requirements.txt              # Python dependencies file
tool.py                       # Automation tool script
```

## Workflow Overview 🚀

### 1. `generate.yml`
This GitHub Actions workflow is used for automatically generating and updating README files. The main steps include:

- Checking out the code
- Setting up a Python 3.8 environment
- Installing required dependencies (`requests`, `openai`, `GitPython`)
- Running the script (`tool.py generate`) to generate or update the README file
- Configuring Git and pushing the updated README file

This process simplifies the maintenance of README files, allowing you to focus on more important matters! 😎

### 2. `optimize.yml`
This workflow automatically optimizes README files and can be triggered manually via the `workflow_dispatch` event. Key steps include:

- Checking out the code
- Setting up a Python 3.8 environment
- Installing dependencies
- Running the script (`tool.py optimize`) to enhance README content
- Committing and pushing the updated README file

Let’s work together to improve content quality! 💪

### 3. `translate.yml`
This workflow automatically translates README files to ensure your project reaches a broader audience. Steps include:

- Checking out the code
- Setting up a Python 3.8 environment
- Installing dependencies
- Running the translation script (`tool.py`)

It's your ultimate assistant in a multilingual era! 🌍

## License 📄
This project is licensed under the Apache License 2.0, allowing you to use, modify, and distribute the code while protecting your rights and obligations.

## Configuration Management 🛠️
The `config.json` file defines important settings, such as API endpoints and supported translation languages, to ensure the smooth operation of the tool and support multilingual functionality. 🤓

## Dependency Management 🐍
The `requirements.txt` file lists the necessary Python packages, including:

- **requests**: Simplifies HTTP requests
- **openai**: Accesses the OpenAI API for various operations
- **GitPython**: Interacts with Git repositories in Python

Please make sure to install these dependencies for the tool to run smoothly! 🌟

## How to Use?

You can either fork this project and use `GitHub Actions` or clone it locally.

Here’s an example using GitHub Actions:

1. Add `PAT` and `OPENAI_API_KEY` in GitHub Secrets.
2. Edit `config.json` to configure the relevant parameters.
3. If you want to generate and translate the README file:
   - Manually run the `generate` workflow, which will create a `.README.md` file in the root directory of the repository.
   - Review and modify the file before committing.
   - Manually trigger the `translate` workflow; the tool will add the edited README to the target repository and generate the translated version.

You're all set! 🎉

If you already have a README file and only want a translation:
- Push it to the `.README.md` file in the tool's repository.
- Manually trigger the `translate` workflow.

You're all set! 🎉

## Feedback and Contributions 🙌
We welcome your feedback and suggestions! Feel free to star⭐️ this project and get involved to help improve its quality and usability.

Thank you for your attention and support! Let’s work together to make README files more vibrant and engaging! 🎉