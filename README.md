# 📚 自动化 README 生成与翻译工具

欢迎来到 **README 自动化生成与翻译工具** 项目！🎉 这个项目的目的是帮助开发者和项目维护者轻松地生成、优化和翻译他们的 README 文件，从而确保文档始终保持最新状态。无论你是新手还是专家，只需轻松点击几下，即可获取一份专业、引人入胜的 README 文档！ 🚀

## 📂 项目结构

```plaintext
./
└── workflows/
│   ├── generate.yml      # 自动生成 README 文件的工作流
│   ├── optimize.yml      # 自动优化 README 文档的工作流
│   └── translate.yml      # 自动翻译 README 文档的工作流
└── LICENSE                    # Apache 许可证文件
└── README.md                  # 项目的自述文件
└── config.json                # 配置文件，定义项目参数
└── requirements.txt          # Python 依赖包列表
└── tool.py                    # 自动化处理工具
```

## ⚙️ 文件简介

### .github/workflows/generate.yml
这是一个 GitHub Actions 工作流，用于自动生成项目的 README 文件。它通过手动触发 (workflow_dispatch) 启动，并执行以下步骤：
1. 检出项目代码；
2. 设置 Python 3.8 环境；
3. 安装必要的依赖 (`requests`, `openai`, `GitPython`)；
4. 执行 `tool.py generate` 脚本生成 README 文件。

### .github/workflows/optimize.yml
该工作流用于自动优化 README 文件，使用 GitHub Actions 手动启动。其主要步骤包括：
1. 检出代码；
2. 设置 Python 3.8 环境；
3. 安装所需依赖；
4. 执行 `tool.py optimize`，利用 OpenAI API 进行优化。

### .github/workflows/translate.yml
这个工作流是用于自动翻译项目的 README 文件，通过手动触发启动。具体步骤包括：
1. 检出代码；
2. 设置 Python 3.8 环境；
3. 安装依赖；
4. 执行 `tool.py translate` 进行翻译。

### LICENSE
包含 Apache 许可证，第 2 版，允许用户自由使用、修改和分发项目，但需遵守相关条件，保护原作者和贡献者的权益。

### config.json
配置文件，定义项目运行所需的参数，包括仓库信息、API 基本网址、模型以及支持的翻译语言。

### requirements.txt
列出项目所需的 Python 包，包括：
- `requests`: 处理 HTTP 请求，简化网络数据交互。
- `openai`: 交互 OpenAI API，实现 AI 模型的使用。
- `GitPython`: 操作 Git 仓库的库。

### tool.py
自动化处理 README 的核心脚本，主要功能包括：
1. 加载配置；
2. 获取仓库内容；
3. 生成 README 内容；
4. 优化和翻译 README；
5. 提交变更；
6. 提供命令行接口。

## 🌸 如何使用？
你可以选择fork本项目后使用`GitHub Actions`或者git到本地使用

这里以前者为示例，选择本地的请自行配置并调整代码

首先语言添加`PAT`和`OPENAI_API_KET`到secrets

然后进入config.json配置相关参数

如果希望生成一个readme请手动触发generate工作流

如果希望修缮一个粗糙的readme请手动触发optimize工作流

如果希望翻译一个readme请手动触发translate工作流

## 🌟 让我们开始吧！

别再犹豫了！用这个工具来提升你的项目文档质量，吸引更多的协作与关注！如果你觉得这个项目对你有帮助，请给我们一个 💖 Star！大家一起努力，让开源社区更加美好！🌈

## 📄 许可证

本项目采用 Apache 许可证，详细信息请查看 [LICENSE](LICENSE) 文件。

欢迎加入，我们一起让 README 变得更简单！🚀