- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)

# 自動生成と翻訳 README ツール 🛠️✨

ようこそ **自動生成と翻訳 README ツール** プロジェクトへ！本ツールは、GitHub リポジトリ内の README ファイルの管理と翻訳を簡素化し、向上させることを目指しています。プロジェクトのメンテナーであれ新しいユーザーであれ、あなたの作業フローをより効率的で楽しいものにします！😄

## プロジェクト構造 🗂️

以下はディレクトリ構造で、各ファイルやフォルダーの用途を迅速に理解するのに役立ちます：

```
.github
└── workflows
    ├── generate.yml         # README ファイルを自動生成するワークフロー
    ├── optimize.yml         # README ファイルを自動最適化するワークフロー
    └── translate.yml        # README ファイルを自動翻訳するワークフロー

LICENSE                        # プロジェクトのライセンスファイル
README.md                     # プロジェクトのメイン README ファイル
README
├── README_Deutsch.md        # ドイツ語 README
├── README_English.md        # 英語 README
├── README_Español.md        # スペイン語 README
├── README_Français.md       # フランス語 README
├── README_日本語.md         # 日本語 README
└── README_繁体中文.md      # 中国語（繁体）README

config.json                   # 設定ファイル
requirements.txt              # Python 依存ファイル
tool.py                       # 自動化ツールスクリプト
```

## ワークフロー概要 🚀

### 1. `generate.yml`
この GitHub Actions ワークフローは README ファイルを自動生成・更新します。主なステップは以下の通りです：

- コードのチェックアウト
- Python 3.8 環境の設定
- 必要な依存関係のインストール（`requests`、`openai`、`GitPython`）
- スクリプト（`tool.py generate`）を実行して README ファイルを生成または更新
- Git を設定し、更新された README ファイルをプッシュ

このプロセスは README ファイルの管理を簡素化し、より重要なことに集中できるようにします！😎

### 2. `optimize.yml`
このワークフローは README ファイルを自動的に最適化し、同様に `workflow_dispatch` イベントによって手動でトリガーできます。主要なステップは：

- コードのチェックアウト
- Python 3.8 環境の設定
- 依存関係のインストール
- スクリプト（`tool.py optimize`）を実行して README コンテンツを向上
- 更新された README ファイルをコミットし、プッシュ

一緒に内容の質を向上させましょう！💪

### 3. `translate.yml`
このワークフローは README ファイルを自動翻訳し、あなたのプロジェクトがより広いオーディエンスにリーチできるようにします。ステップは以下の通りです：

- コードのチェックアウト
- Python 3.8 環境の設定
- 依存関係のインストール
- 翻訳スクリプト（`tool.py`）を実行

それは多言語時代におけるあなたの究極のアシスタントです！🌍

## ライセンス 📄
本プロジェクトは Apache License 2.0 に従い、コードの使用、修正、配布を許可し、あなたの権利と義務を保護します。

## 設定管理 🛠️
`config.json` ファイルは API エンドポイントやサポートされている翻訳言語などの重要な設定を定義し、ツールの円滑な運用と多言語機能のサポートを保証します。🤓

## 依存管理 🐍
`requirements.txt` ファイルには必要な Python パッケージがリストアップされています：

- **requests**：HTTP リクエストを簡素化
- **openai**：さまざまな操作のために OpenAI API にアクセス
- **GitPython**：Python 内で Git リポジトリと対話

これらの依存関係をインストールして、ツールを円滑に運用してください！🌟

## 使い方

このプロジェクトをフォークして `GitHub Actions` を使用するか、ローカルにクローンして使用することができます。

以下は GitHub Actions を使用する例です：

1. GitHub Secrets に `PAT` と `OPENAI_API_KEY` を追加します。
2. `config.json` を編集して設定関連のパラメーターを構成します。
3. README ファイルを生成して翻訳したい場合：
   - 手動で `generate` ワークフローを実行し、リポジトリのルートディレクトリに `.README.md` ファイルを生成します。
   - そのファイルをレビューおよび編集後、コミットします。
   - 手動で `translate` ワークフローをトリガーし、ツールが編集した README をターゲットリポジトリに追加し、翻訳版を生成します。

完了です！🎉

もしすでに README ファイルが用意されていて、単に翻訳を希望する場合：
- それをツールリポジトリの `.README.md` ファイルにプッシュします。
- 手動で `translate` ワークフローをトリガーします。

完了です！🎉

## フィードバックと貢献 🙌
私たちはあなたのフィードバックや提案を歓迎します！ぜひこのプロジェクトにいいね⭐️をつけて、一緒に参加し、プロジェクトの質と有用性を向上させましょう。

ご注目とご支援、ありがとうございます！一緒に README ファイルをより生き生きと楽しいものにしていきましょう！🎉