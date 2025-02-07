[Back to main language README](README.md)

# README: README-Automatic-Generation-and-Translation-Tool 📄🌍

## Project Introduction ✨

Welcome to the **README-Automatic-Generation-and-Translation-Tool** project! This tool aims to simplify the process of generating and translating README files for GitHub repositories. By combining the GitHub API and OpenAI API, our tool can automatically generate comprehensive README documents and support translations in multiple languages, making your project more accessible and understandable to users around the world.

## Features 🚀

- **Automated Configuration Management**: Load settings from a configuration file.
- **GitHub API Interaction**: Fetch file contents from specified GitHub repositories.
- **OpenAI API Integration**: Use OpenAI API to extract file content and generate engaging README text and translations.
- **Multi-language Support**: Generate translated versions based on predefined language configurations.
- **README Management**: Build README files that include project overview, installation steps, and link translated versions.
- **Version Control**: Automatically commit changes to GitHub repository after generating the README and its translations, maintaining version control.

## Installation Steps ⚙️

Before using this tool, please ensure you have the following dependencies installed:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Delta-Water/README-Automatic-Generation-and-Translation-Tool.git
   cd README-Automatic-Generation-and-Translation-Tool
   ```

2. **Install Dependencies**:
   Use `pip` to install the required libraries for the project:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration File**: Create or edit the `config.json` file in the project root directory to set the API URL and other configuration options.

4. **Set Up GitHub Key**: Configure your personal access token in the "Secrets" section of GitHub, allowing the tool to access your GitHub repository.

## Usage Instructions 📋

1. **Configuration**: Ensure the `config.json` file is correctly configured with the Base API URL, main branch, and primary programming language index.

2. **Run the Tool**: Execute the following command to start the tool:
   ```bash
   python tool.py
   ```

3. **Manually Trigger GitHub Actions**: You can also manually run GitHub Actions or configure it to run automatically upon new commits.

## Contribution Guidelines 🤝

We welcome contributions in any form! Please follow these steps:
1. **Fork this repository**.
2. **Create your feature branch**:
   ```bash
   git checkout -b feature/MyFeature
   ```
3. **Commit your changes**:
   ```bash
   git commit -m "Add some feature"
   ```
4. **Push to the branch**:
   ```bash
   git push origin feature/MyFeature
   ```
5. **Submit a pull request**.

Thank you for supporting this project! If you have any questions or suggestions, please create an issue or contact the project maintainers. 🙏

## License 📜

This project follows the **Apache License, Version 2.0**. Please refer to the relevant documents for detailed terms and conditions to ensure legality and fairness in collaboration and use.

---

Thank you for using the **README-Automatic-Generation-and-Translation-Tool**! Let's make open source more open and collaborative together! 💪