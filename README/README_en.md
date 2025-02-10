<div align="center">

[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Automated README Generation and Translation Tool

Welcome to the **Automated README Generation and Translation Tool** project! 🎉 This project aims to provide developers and project maintainers with an easy way to seamlessly create, optimize, and translate README files. Whether you're a beginner or an expert, you can get a professional and engaging README document in just a few simple steps! 🚀

## 📂 Project Structure

```plaintext
./
└── workflows/
│   ├── generate.yml      # Workflow for automatically generating README files
│   ├── optimize.yml      # Workflow for automatically optimizing README documents
│   └── translate.yml      # Workflow for automatically translating README documents
└── LICENSE                # Apache License file
└── README.md              # Project README file
└── config.json            # Configuration file that defines project parameters
└── requirements.txt       # List of Python dependencies
└── tool.py                # Automation processing tool
```

## ⚙️ File Overview

### `.github/workflows/generate.yml`
This workflow automatically generates the project's README file using GitHub Actions. When manually triggered, it performs the following steps:
1. Checks out the project code;
2. Sets up a Python 3.8 environment;
3. Installs required dependencies (`requests`, `openai`, `GitPython`);
4. Executes the `tool.py generate` script to generate the README file.

### `.github/workflows/optimize.yml`
This workflow is for automatically optimizing the README file. Upon manual triggering, it primarily performs the following steps:
1. Checks out the code;
2. Sets up a Python 3.8 environment;
3. Installs necessary dependencies;
4. Runs `tool.py optimize`, optimizing the document through the OpenAI API.

### `.github/workflows/translate.yml`
This workflow automatically translates the project's README file and is also started by manual trigger. Steps include:
1. Checks out the code;
2. Sets up a Python 3.8 environment;
3. Installs dependencies;
4. Executes `tool.py translate` for translation.

### `LICENSE`
This file contains the Apache License, Version 2.0, which allows users to freely use, modify, and distribute this project under certain conditions, ensuring the rights of the original authors and contributors are protected.

### `config.json`
This configuration file defines various parameters needed for the project's operation, including repository information, API base URLs, models, and supported translation languages.

### `requirements.txt`
Lists the necessary Python packages for the project, including:
- `requests`: for handling HTTP requests and simplifying network interactions.
- `openai`: for interacting with the OpenAI API to invoke AI models.
- `GitPython`: to provide support for operations on Git repositories.

### `tool.py`
The core script for automating the README processing, with main functionalities including:
1. Loading configurations;
2. Fetching repository content;
3. Generating README content;
4. Improving and translating the README;
5. Committing changes;
6. Providing a command-line interface.

## 🌸 How to Use?

You can either fork this project to use `GitHub Actions` or clone it locally for use. Here's how to proceed with the former; for the latter, please configure accordingly.

1. First, add `PAT` and `OPENAI_API_KEY` to your Secrets.
2. Next, enter relevant parameters in `config.json`.
3. To generate the README, manually trigger the `generate` workflow.
4. To optimize the README, manually trigger the `optimize` workflow.
5. To translate the README, manually trigger the `translate` workflow.

## 🌟 Let's Get Started!

Don’t hesitate any longer! Use this tool to enhance the quality of your project documentation and attract more collaboration and attention! If you find this project helpful, please give us a 💖 Star! Let's work together to make the open-source community even better! 🌈

## 📄 License

This project is licensed under the Apache License. Please refer to the [LICENSE](LICENSE) file for more details.

Join us in making README creation easier and more efficient! 🚀