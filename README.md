# 📚 自动化 README 生成与翻译工具

欢迎来到 **README 自动化生成与翻译工具** 项目！🎉 本项目旨在为开发者和项目维护者提供一个便捷的方式，轻松生成、优化和翻译 README 文件。无论你是新手还是专家，只需简单几步，即可获得一份专业、引人入胜的 README 文档！ 🚀

## 📂 项目结构

```plaintext
./
└── workflows/
│   ├── generate.yml      # 自动生成 README 文件的工作流
│   ├── optimize.yml      # 自动优化 README 文档的工作流
│   └── translate.yml      # 自动翻译 README 文档的工作流
└── LICENSE                # Apache 许可证文件
└── README.md              # 项目的自述文件
└── config.json            # 配置文件，定义项目参数
└── requirements.txt       # Python 依赖包列表
└── tool.py                # 自动化处理工具
```

## ⚙️ 文件简介

### `.github/workflows/generate.yml`
该工作流通过 GitHub Actions 进行项目 README 文件的自动生成。手动触发后，它执行以下步骤：
1. 检出项目代码；
2. 设置 Python 3.8 环境；
3. 安装所需依赖（`requests`、`openai`、`GitPython`）；
4. 执行 `tool.py generate` 脚本生成 README 文件。

### `.github/workflows/optimize.yml`
此工作流用于自动优化 README 文件，手动触发后，主要执行以下步骤：
1. 检出代码；
2. 设置 Python 3.8 环境；
3. 安装必要依赖；
4. 执行 `tool.py optimize`，通过 OpenAI API 进行优化处理。

### `.github/workflows/translate.yml`
该工作流用于自动翻译项目的 README 文件，同样通过手动触发启动。步骤包括：
1. 检出代码；
2. 设置 Python 3.8 环境；
3. 安装依赖；
4. 执行 `tool.py translate` 进行翻译。

### `LICENSE`
此文件包含 Apache 许可证第 2 版，允许用户在遵守相关条件下，自由使用、修改和分发本项目，以保护原作者和贡献者的权益。

### `config.json`
此配置文件定义了项目运行所需的各种参数，包括仓库信息、API 基础网址、模型及支持的翻译语言。

### `requirements.txt`
列出项目所需的 Python 包，包括：
- `requests`: 用于处理 HTTP 请求，简化网络交互。
- `openai`: 与 OpenAI API 进行交互，实现 AI 模型的调用。
- `GitPython`: 提供对 Git 仓库的操作支持。

### `tool.py`
核心脚本用于自动化处理 README，主要功能包括：
1. 加载配置；
2. 获取仓库内容；
3. 生成 README 内容；
4. 完善和翻译 README；
5. 提交变更；
6. 提供命令行接口。

## 🌸 如何使用？

你可以选择 Fork 本项目后使用 `GitHub Actions`，或者将其克隆到本地进行使用。以下将以前者为例，后者请自行配置。

1. 首先，将 `PAT` 和 `OPENAI_API_KEY` 添加到 Secrets 中。
2. 接着，进入 `config.json` 配置相关参数。
3. 如需生成 README，请手动触发 `generate` 工作流。
4. 如需优化 README，请手动触发 `optimize` 工作流。
5. 如需翻译 README，请手动触发 `translate` 工作流。

## 🌟 让我们开始吧！

别再犹豫了！使用这个工具提升你的项目文档质量，吸引更多的协作与关注！如果你觉得这个项目对你有帮助，请给我们一个 💖 Star！让我们共同努力，让开源社区更加美好！🌈

## 📄 许可证

本项目采用 Apache 许可证，详细信息请查看 [LICENSE](LICENSE) 文件。

欢迎加入我们，让 README 变得更加简单高效！🚀