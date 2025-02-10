<div align="center">

[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Español](/README/README_es.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md)

</div>

# 📚 README 自動生成と翻訳ツール

ようこそ **README 自動生成と翻訳ツール** プロジェクトへ！🎉 本プロジェクトは、開発者やプロジェクトメンテナンス担当者に便利な方法を提供し、簡単に README ファイルを生成、最適化、翻訳できるようにすることを目的としています。初心者でも専門家でも、簡単なステップでプロフェッショナルで魅力的な README ドキュメントを手に入れることができます！ 🚀

## 📂 プロジェクト構成

```plaintext
./
└── workflows/
│   ├── generate.yml      # 自動生成 README ファイルのワークフロー
│   ├── optimize.yml      # README ドキュメントの自動最適化ワークフロー
│   └── translate.yml      # README ドキュメントの自動翻訳ワークフロー
└── LICENSE                # Apache ライセンスファイル
└── README.md              # プロジェクトの自述ファイル
└── config.json            # プロジェクトパラメータを定義する設定ファイル
└── requirements.txt       # Python 依存パッケージリスト
└── tool.py                # 自動処理ツール
```

## ⚙️ ファイル概要

### `.github/workflows/generate.yml`
このワークフローは GitHub Actions を使用してプロジェクトの README ファイルを自動生成します。手動でトリガーした後、以下のステップを実行します：
1. プロジェクトコードをチェックアウト；
2. Python 3.8 環境を設定；
3. 必要な依存関係をインストール（`requests`、`openai`、`GitPython`）；
4. `tool.py generate` スクリプトを実行して README ファイルを生成。

### `.github/workflows/optimize.yml`
このワークフローは README ファイルを自動最適化するためのもので、手動でトリガーすると、主に以下のステップを実行します：
1. コードをチェックアウト；
2. Python 3.8 環境を設定；
3. 必要な依存関係をインストール；
4. `tool.py optimize` を実行し、OpenAI API を通じて最適化処理を行います。

### `.github/workflows/translate.yml`
このワークフローはプロジェクトの README ファイルを自動翻訳するためのもので、同様に手動でトリガーします。ステップは次の通りです：
1. コードをチェックアウト；
2. Python 3.8 環境を設定；
3. 依存関係をインストール；
4. `tool.py translate` を実行して翻訳します。

### `LICENSE`
このファイルには Apache ライセンス第 2 版が含まれており、ユーザーが関連する条件を遵守する限り、自由にこのプロジェクトを使用、改変、配布できることを許可し、原作者と貢献者の権利を保護します。

### `config.json`
この設定ファイルは、プロジェクトの実行に必要なさまざまなパラメータを定義しています。これにはリポジトリ情報、API 基本 URL、モデル、およびサポートされる翻訳言語が含まれます。

### `requirements.txt`
プロジェクトで必要な Python パッケージをリストします：
- `requests`: HTTP リクエストを処理し、ネットワークのやり取りを簡素化します。
- `openai`: OpenAI API と連携し、AI モデルの呼び出しを実現します。
- `GitPython`: Git リポジトリの操作をサポートします。

### `tool.py`
README の自動処理に使用されるコアスクリプトで、主な機能は次のとおりです：
1. 設定を読み込む；
2. リポジトリの内容を取得する；
3. README 内容を生成する；
4. README を完成させ、翻訳する；
5. 変更をコミットする；
6. コマンドラインインターフェースを提供する。

## 🌸 使用方法

このプロジェクトを Fork して `GitHub Actions` を利用するか、ローカルにクローンして使用できます。以下では前者を例に説明します。後者については自分で設定してください。

1. まず、`PAT` と `OPENAI_API_KEY` を Secrets に追加します。
2. 次に、`config.json` に関連するパラメータを設定します。
3. README を生成するには、手動で `generate` ワークフローをトリガーします。
4. README を最適化するには、手動で `optimize` ワークフローをトリガーします。
5. README を翻訳するには、手動で `translate` ワークフローをトリガーします。

## 🌟 さあ、始めましょう！

もう迷うことはありません！このツールを使ってプロジェクトのドキュメント品質を向上させ、より多くの協力や関心を引きましょう！このプロジェクトが役に立ったと感じたら、ぜひ 💖 Star をください！一緒に努力してオープンソースコミュニティをより良いものにしましょう！🌈

## 📄 ライセンス

本プロジェクトは Apache ライセンスの下に提供されており、詳細情報は [LICENSE](LICENSE) ファイルを参照してください。

私たちと一緒に README をよりシンプルで効率的にしましょう！🚀