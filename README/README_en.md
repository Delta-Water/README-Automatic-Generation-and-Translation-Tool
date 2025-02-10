<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 Automated README Generation and Translation Tool

Welcome to the **Automated README Generation and Translation Tool** project! 🎉 This project aims to provide developers and project maintainers with an easy way to generate, optimize, and translate README files effortlessly. Whether you're a beginner or an expert, with just a few simple steps, you'll have a professional and engaging README document! 🚀

## 📂 Project Structure

```plaintext
./
└── workflows/
│   ├── generate.yml      # Workflow for automatically generating README files
│   ├── optimize.yml      # Workflow for automatically optimizing README documents
│   └── translate.yml      # Workflow for automatically translating README documents
└── LICENSE                # Apache license file
└── README.md              # Project's README file
└── config.json            # Configuration file defining project parameters
└── requirements.txt       # List of Python dependencies
└── tool.py                # Automation processing tool
```

## ⚙️ File Descriptions

### `.github/workflows/generate.yml`
This workflow automatically generates the project's README file using GitHub Actions. Once manually triggered, it performs the following steps:
1. Checks out the project's code;
2. Sets up the Python 3.8 environment;
3. Installs required dependencies (`requests`, `openai`, `GitPython`);
4. Executes the `tool.py generate` script to create the README file.

### `.github/workflows/optimize.yml`
This workflow is used for automatically optimizing the README file. When manually triggered, it mainly performs the following steps:
1. Checks out the code;
2. Sets up the Python 3.8 environment;
3. Installs necessary dependencies;
4. Executes `tool.py optimize`, optimizing the content via the OpenAI API.

### `.github/workflows/translate.yml`
This workflow automatically translates the project's README file, also initiated by a manual trigger. The steps include:
1. Checks out the code;
2. Sets up the Python 3.8 environment;
3. Installs dependencies;
4. Executes `tool.py translate` for translation.

### `LICENSE`
This file includes the Apache License Version 2.0, allowing users to freely use, modify, and distribute this project under certain conditions, thereby protecting the rights of the original authors and contributors.

### `config.json`
This configuration file defines various parameters required for the project to run, including repository information, API base URLs, models, and supported translation languages.

### `requirements.txt`
Lists the Python packages required for the project, including:
- `requests`: For handling HTTP requests and simplifying network interactions.
- `openai`: For interacting with the OpenAI API to invoke AI models.
- `GitPython`: Provides support for operating on Git repositories.

### `tool.py`
The core script for automating README processing, with key functions including:
1. Loading configuration;
2. Retrieving repository content;
3. Generating README content;
4. Refining and translating the README;
5. Committing changes;
6. Providing a command-line interface.

## 🌸 How to Use?

You can either fork this project to use `GitHub Actions` or clone it locally for use. The following steps are based on the former; for the latter, please configure accordingly.

1. First, add your `PAT` and `OPENAI_API_KEY` to the Secrets.
2. Then, navigate to `config.json` to set the relevant parameters.
3. To generate a README, manually trigger the `generate` workflow.
4. To optimize the README, manually trigger the `optimize` workflow.
5. To translate the README, manually trigger the `translate` workflow.

## 🌟 Let's Get Started!

Don’t hesitate any longer! Use this tool to enhance the quality of your project documentation and attract more collaboration and attention! If you find this project helpful, give us a 💖 Star! Together, let’s make the open-source community even better! 🌈

## 📄 License

This project is licensed under the Apache License; for detailed information, please see the [LICENSE](LICENSE) file.

Join us in making README generation more efficient and effective! 🚀