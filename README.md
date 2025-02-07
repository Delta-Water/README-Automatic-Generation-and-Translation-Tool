## README

### 语言切换
- [简体中文](README.md)
- [繁体中文](README/README_繁体中文.md)
- [English](README/README_English.md)
- [Español](README/README_Español.md)
- [Français](README/README_Français.md)
- [Deutsch](README/README_Deutsch.md)
- [日本語](README/README_日本語.md)

# 自动生成与翻译工具 🚀

## 项目介绍 📖

欢迎使用**自动生成与翻译工具**！这个工具旨在简化文档的自动创作和翻译过程，特别是为GitHub项目生成README文件及其多语言版本。它集成了OpenAI的API，能够总结文件内容并生成高质量的README文件，同时提供多种语言的翻译服务。

## 功能特点 🔍

- **配置加载**：从`config.json`文件中加载配置信息，包括仓库名称、所有者和主要使用的编程语言。
- **与GitHub交互**：通过GitHub API检索指定仓库中的文件，并获取每个文件的内容。
- **OpenAI集成**：利用OpenAI API总结文件内容并生成README，支持多语言翻译。
- **文件管理**：创建或更新README文件及其翻译版本，并确保目录结构井然有序。
- **版本控制**：提交更改并将更新后的README和翻译文件推送回GitHub仓库。

## 安装步骤 ⚙️

1. 确保您已经安装了Python及相关依赖。可以使用以下命令进行安装：
   ```bash
   pip install -r requirements.txt
   ```

2. 下载代码，并在项目根目录中配置`config.json`文件。您可以根据您的GitHub仓库的具体信息进行设置。

3. 运行主脚本`tool.py`：
   ```bash
   python tool.py
   ```

## 使用说明 🛠️

1. 编辑`config.json`以适应您的仓库参数，例如：
   ```json
   {
       "repository_name": "您的仓库",
       "owner": "您的用户名",
       "api_base_url": "https://api.github.com",
       "main_branch": "main",
       "primary_language": "python"
   }
   ```
   
2. 执行程序后，工具将自动生成README文件，并将其翻译成您在配置中指定的语言。

3. 更新后的README文件和翻译将被自动推送至您的GitHub仓库。

## 贡献指南 🤝

我们非常欢迎任何形式的贡献！请遵循以下步骤：

1. Fork 本仓库。
2. 创建您的特性分支 (`git checkout -b feature/YourFeature`)。
3. 提交您的更改 (`git commit -m 'Add some feature'`)。
4. 推送到分支 (`git push origin feature/YourFeature`)。
5. 提交合并请求。

## 许可证 📄

本项目基于 [Apache License Version 2.0](http://www.apache.org/licenses/LICENSE-2.0)，在符合该许可证条款下，您可以自由使用、修改和分发本软件及其他作品。

如需了解更多信息，请访问我们的GitHub页面或查看项目文档。

---

感谢您使用我们的工具！如有任何问题，请随时在GitHub上提出问题或浏览相关文档。我们期待您的参与与反馈！🌟