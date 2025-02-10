<div align="center">

[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 📚 自动化 README 生成与翻译工具

欢迎来到 **自动化 README 生成与翻译工具** 的世界！🎉 本项目旨在为开发者和项目维护者提供一个高效便捷的解决方案，轻松生成、优化和翻译 README 文件，为代码提供专业且引人入胜的文档。无论您是新手还是经验丰富的开发者，这里都有您所需的工具！🌟

## 🛠️ 项目结构

以下是项目的基本结构，一目了然，方便您的使用：

```
.
├── .github
│   └── workflows
│       ├── generate.yml      # 自动生成 README 文件的工作流程
│       ├── optimize.yml      # 优化 README 文件的工作流程
│       └── translate.yml      # 翻译 README 文件的工作流程
├── LICENSE                   # 项目许可证
├── README.md                 # 项目说明文件
├── config.json               # 工具配置文件
├── requirements.txt          # 依赖库列表
└── tool.py                   # 自动化脚本
```

## ✨ 核心功能

1. **自动化 README 生成**：借助 GitHub Actions 工作流程，从项目代码中自动生成专业的 README 文件。
2. **优化功能**：通过 OpenAI 的 API，实现 AI 驱动的优化，提升现有 README 文档的质量。
3. **翻译能力**：自动将 README 文件翻译成多种语言，助力更广泛的受众轻松访问您的项目👌。

## ⚙️ 工作流

### 1. `generate.yml`
- 手动触发，通过 `workflow_dispatch` 生成 README 文件。
- 在 Ubuntu 环境下运行，安装所需依赖（`requests`, `openai`, `GitPython`）。
- 最后执行 `tool.py generate` 脚本，生成专业的 README。

### 2. `optimize.yml`
- 手动触发，自动优化现有 README 文件。
- 包含代码检查、Python 环境设置和依赖安装的步骤。
- 执行 `tool.py optimize` 脚本，提升 README 的可读性。

### 3. `translate.yml`
- 手动触发，自动翻译 README 文件。
- 检出代码、设置 Python 环境、安装所需依赖后，运行翻译脚本。

## 📝 配置说明

`config.json` 文件包含了工具的基本配置和选项，包括：
- 仓库名称和所有者
- API 的基本 URL 和所用语言模型
- 需要翻译的语言及其缩写
- …

请确保正确配置此文件，以确保工具的正常运行。🔑

## 📦 依赖库

在 `requirements.txt` 中您可以找到项目所需的依赖库：
- **requests**：用户友好的 HTTP 请求库。
- **openai**：与 OpenAI 的 API 交互的库。
- **GitPython**：用于与 Git 仓库交互的 Python 库。

请确保安装这些依赖，以顺利运行项目！🚀

## 🖥️ 关键功能详解

`tool.py` 脚本是本项目的核心，提供了以下功能：
- 自动加载配置文件，管理项目设置。
- 交互式获取仓库文件并生成文件摘要。
- 创建、优化和翻译 README 文件，并通过 Git 操作进行提交。

您还可以通过命令行界面灵活执行特定命令，以满足不同需求！🎈

## 🌸 如何使用？

您可以选择 fork 本项目，使用 `GitHub Actions`，或者克隆到本地使用。以下以使用 `GitHub Actions` 为例：

1. 将 `PAT` 和 `OPENAI_API_KEY` 添加到 secrets。
2. 进入 `config.json` 配置相关参数。
3. 手动触发想要执行的工作流即可。

请注意，`optimize.yml` 和 `translate.yml` 需要在目标仓库中已有 README 文件才能执行。

## 📜 许可证

本项目遵循 **Apache License 2.0** 许可证，详见 `LICENSE` 文件。

## 🤝 贡献与支持

我们非常欢迎您的贡献！如果您觉得这个工具对您有帮助，请给我们一个 ⭐️。您的支持是我们不断前行的动力！💪

---

通过这个工具，您可以轻松创建专业、易读的文档。快来试试吧，省时省力，这个项目值得您收藏！🌟