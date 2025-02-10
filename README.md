<p align="center">

[繁体中文](/README/README_zh-TW.md) | [English](/README/README_en.md) | [Español](/README/README_es.md) | [Français](/README/README_fr.md) | [Deutsch](/README/README_de.md) | [日本語](/README/README_ja.md)

</p>

# 🤖 自动生成与翻译 README 工具

欢迎来到 **README-Automatic-Generation-and-Translation-Tool** 项目! 🎉 这个项目旨在简化您的 GitHub 项目文档生成与翻译工作，让您的 README 文件更加专业和多语言化，无论您身在何处，都能轻松吸引更多的开发者！🌍✨

## 🚀 项目结构

以下是项目的结构概览：

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # GitHub Actions 工作流文件
│
├── LICENSE            # Apache 许可证 2.0
│
├── README.md          # 项目的主要 README 文件
│
├── README/
│   ├── README_Deutsch.md     # 德语 README 
│   ├── README_English.md      # 英语 README 
│   ├── README_Español.md      # 西班牙语 README 
│   ├── README_Français.md     # 法语 README 
│   ├── README_日本語.md        # 日语 README 
│   └── README_繁体中文.md      # 繁体中文 README 
│
├── config.json       # 配置文件，包括设定与翻译语言
│
├── requirements.txt   # 项目所需的依赖库
│
└── tool.py            # 自动生成与翻译 README 的主要脚本
```

## 📜 许可证概要

我们的项目采用 **Apache 许可证 2.0**，这意味着您可以自由使用、修改和分发我们的代码，但需保留原始许可证和相关声明。📝 让我们共同促进开源合作吧！💪

## ⚙️ 配置文件

`config.json` 是您项目的配置中心。它允许您设置相关参数，如仓库名称、所有者信息及支持的翻译语言（简体中文、繁体中文、英语、西班牙语、法语、德语、日语），让您能轻松切换和管理多语言内容。🌐💻

## 📦 依赖库

我们的项目依赖以下库，确保您可以轻松搭建开发环境：

1. **requests** - 简单的HTTP请求库。
2. **openai** - 与 OpenAI API 交互的库。
3. **GitPython** - 通过 Python 操作 Git 仓库的库。

您只需要运行以下命令安装依赖：

```bash
pip install -r requirements.txt
```

## ⚙️ 功能概述

脚本 `tool.py` 提供了强大的功能，包括：

1. **配置加载** - 从配置文件中读取项目参数。
2. **仓库交互** - 通过 GitHub API 获取仓库文件及其内容。
3. **内容摘要** - 利用 OpenAI 的 API 摘要仓库文件内容，生成简洁的描述。
4. **README 生成** - 根据文件结构与摘要信息生成专业的 README 文件。
5. **翻译** - 将 README 内容翻译成多种语言，保留活泼的表情符号和样式。😄🎨
6. **Git 操作** - 提交更新后的 README 和翻译文件到仓库。

## 🚀 开启之旅

只需手动启动 GitHub Actions 工作流，等待几分钟，优秀的 README 文件将自动生成并翻译好，您可以尽情享受这一切的美好。✨

### 🌟 快来为我们加星吧！您的支持是我们不断前进的动力！💖

感谢您的关注和支持！如有任何问题或建议，请随时在GitHub上与我们联系。我们期待着与您共同创造更美好的开源社区！🤝