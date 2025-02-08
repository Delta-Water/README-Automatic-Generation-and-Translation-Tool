- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# README - 自动化生成与翻译工具 🌟

欢迎来到 **README-Automatic-Generation-and-Translation-Tool** 项目！🚀

我们致力于为开发者提供一个自动化工具，以轻松生成和翻译GitHub项目的README文件，让你的项目文档更具吸引力和专业感！💕 

## 项目结构 📂

以下是当前项目的结构，对于不同文件的说明如下：

```
├── .github
│   └── workflows
│       └── main.yml     # GitHub Actions工作流配置文件
├── LICENSE                # 项目许可证文件
├── README.md              # 项目的主要文档
├── README
│   ├── README_Deutsch.md  # 德语README文件
│   ├── README_English.md  # 英语README文件
│   ├── README_Español.md  # 西班牙语README文件
│   ├── README_Français.md # 法语README文件
│   ├── README_日本語.md    # 日语README文件
│   └── README_繁体中文.md   # 繁体中文README文件
├── config.json            # 项目配置文件
├── requirements.txt       # Python依赖库列表
└── tool.py                # 自动生成和更新README文件的脚本
```

## 文件摘要 📄

### 1. `.github/workflows/main.yml`
这个GitHub Actions工作流配置文件帮助我们实现了README文件的生成和翻译自动化。它在最新版本的Ubuntu环境中运行，执行以下步骤：

- **代码检出**：获取最新的代码。
- **设置Python**：配置Python 3.8作为环境。
- **安装依赖**：升级pip并安装所需的Python包（requests、openai、GitPython）。
- **运行脚本**：执行Python脚本（tool.py），使用GitHub和OpenAI API凭据生成README。

### 2. `LICENSE`
该文件包含Apache许可证版本2.0，概述了使用、复制和分发软件和其他作品的条款与条件。许可证提供了法律框架，促进开源软件开发，保护贡献者和用户的权益。

### 3. `config.json`
这个配置文件定义了项目的重要参数，如：仓库名称、拥有者、基本API URL和默认分支（main）。它支持自动生成和翻译README文件。

### 4. `requirements.txt`
列出了Python项目所需的依赖库，包括：

- **requests**：简化HTTP请求的流行库。
- **openai**：与OpenAI API交互的库。
- **GitPython**：直接从Python操作和交互Git仓库的库。

### 5. `tool.py`
这个脚本自动化生成和更新GitHub仓库中的README文件及其翻译。其关键功能包括：

1. **配置与设置**：加载配置，获取必要的环境变量。
2. **文件管理**：访问GitHub仓库，获取文件结构和内容。
3. **README生成**：利用OpenAI的API生成详细的README文件。
4. **翻译创建**：将生成的README翻译成多种语言。
5. **链接与结构集成**：增强可导航性。
6. **提交与推送**：将更新后的文件提交到GitHub仓库。

## 快速开始 🚀

想要参与吗？点击右上角的⭐赞一下我们的项目吧！ 💖 

通过这个工具，我们帮助每个开发者都能轻松维护项目文档，提升项目的国际化水平！无论你的项目是大还是小，我们都能让你在文档方面省去烦恼，共同打造一个更好的开源生态！🌍👩‍💻👨‍💻

如果你有任何问题或建议，请随时与我们联系！happy coding！🎉