# 📚 自动化 README 生成与翻译工具

欢迎来到 **自动化 README 生成与翻译工具** 的世界！🎉 本项目旨在帮助开发者和项目维护者轻松生成、优化和翻译他们的 README 文件，为代码提供专业且引人入胜的文档。无论你是新手还是老手，这里都有你需要的工具！🌟

## 🛠️ 项目结构

以下是项目的基本结构，简单易读，让你一目了然：

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

1. **自动化 README 生成**：利用 GitHub Actions 工作流程，从项目代码中自动生成 README 文件。
2. **优化功能**：使用 OpenAI 的 API，通过 AI 驱动的优化提升现有 README 文档的质量。
3. **翻译能力**：自动翻译 README 文件为多种语言，帮助更广泛的受众轻松访问👌。

## ⚙️ 工作流程

### 1. `generate.yml`
- 手动触发，通过 `workflow_dispatch` 生成 README 文件。
- 在 Ubuntu 环境下运行，安装所需依赖（`requests`, `openai`, `GitPython`）。
- 最后执行 `tool.py generate` 脚本，生成专业的 README。

### 2. `optimize.yml`
- 手动触发，自动优化现有 README 文件。
- 包含检查代码、设置 Python 环境、安装依赖的步骤。
- 执行 `tool.py optimize` 脚本，提升 README 的可读性。

### 3. `translate.yml`
- 手动触发，自动翻译 README 文件。
- 检出代码、设置 Python 环境、安装所需依赖后，运行翻译脚本。

## 📝 配置说明

`config.json` 文件包含了工具的基本配置和选项，包括：
- 仓库名称和所有者
- API 的基本 URL 和所用语言模型
- 支持的翻译语言及其缩写

确保正确配置，此文件是确保工具正常运行的关键！🔑

## 📦 依赖库

在 `requirements.txt` 中可以找到项目所需的依赖库：
- **requests**：一个用户友好的 HTTP 请求库。
- **openai**：与 OpenAI 的 API 交互的库。
- **GitPython**：用于与 Git 仓库交互的 Python 库。

安装这些依赖，确保项目顺利运行！🚀

## 🖥️ 关键功能详解

`tool.py` 脚本是这一切的核心，提供了以下功能：
- 自动加载配置文件，管理你的项目设置。
- 互动式地获取仓库文件，并生成文件摘要。
- 创建、优化和翻译 README 文件，并通过 Git 操作进行提交。

你还可以通过命令行界面灵活执行特定命令，满足不同需求！🎈

## 📜 许可证

本项目遵循 **Apache License 2.0** 许可证。详细信息请参见 `LICENSE` 文件。

## 🤝 贡献与支持

我们非常欢迎你的贡献！如果你觉得这个工具对你有帮助，请给我们一个 ⭐️。你的支持是我们不断前进的动力！💪

---

通过这个工具，创造专业、易读的文档变得轻而易举，赶快试试吧，省时省力，这个项目值得你收藏！🌟