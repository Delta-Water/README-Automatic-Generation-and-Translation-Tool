[zh](/README.md) | [繁体中文](/README/README_zh-TW.md) | [English](/README/README_en.md) | [Español](/README/README_es.md) | [Français](/README/README_fr.md) | [Deutsch](/README/README_de.md)

- [言語を切り替える: 繁体中文](/README/README_繁体中文.md) | - [Switch Language: English](/README/README_English.md) | - [Cambiar idioma: Español](/README/README_Español.md) | - [Changer de langue: Français](/README/README_Français.md) | - [Sprache wechseln: Deutsch](/README/README_Deutsch.md) | - [切換語言: 日本語](/README/README_日本語.md)

# 🤖 自動生成と翻訳の README ツール

ようこそ **README-Automatic-Generation-and-Translation-Tool** プロジェクトへ! 🎉 このプロジェクトは、GitHub プロジェクトの文書生成と翻訳作業を簡素化し、あなたの README ファイルをよりプロフェッショナルで多言語対応にすることを目的としています。どこにいても、もっと多くの開発者を簡単に惹きつけることができます！🌍✨

## 🚀 プロジェクト構造

以下はプロジェクトの構造の概要です：

```
README-Automatic-Generation-and-Translation-Tool/
│
├── .github/
│   └── workflows/
│       └── main.yml  # GitHub Actions ワークフローファイル
│
├── LICENSE            # Apache ライセンス 2.0
│
├── README.md          # プロジェクトの主要 README ファイル
│
├── README/
│   ├── README_Deutsch.md     # ドイツ語 README 
│   ├── README_English.md      # 英語 README 
│   ├── README_Español.md      # スペイン語 README 
│   ├── README_Français.md     # フランス語 README 
│   ├── README_日本語.md        # 日本語 README 
│   └── README_繁体中文.md      # 繁体中文 README 
│
├── config.json       # 設定ファイル、設定と翻訳言語を含む
│
├── requirements.txt   # プロジェクトに必要な依存ライブラリ
│
└── tool.py            # 自動生成と翻訳 README の主要スクリプト
```

## 📜 ライセンス概要

私たちのプロジェクトは **Apache ライセンス 2.0** を採用しており、これはあなたが私たちのコードを自由に使用、変更、配布できることを意味しますが、元のライセンスと関連する表記を保持する必要があります。📝 さあ、一緒にオープンソースの協力を促進しましょう！💪

## ⚙️ 設定ファイル

`config.json` はあなたのプロジェクトの設定センターです。これにより、リポジトリ名、オーナー情報、サポートされている翻訳言語（簡体字中国語、繁体字中国語、英語、スペイン語、フランス語、ドイツ語、日本語）が設定できます。これにより、多言語コンテンツの切り替えと管理が簡単になります。🌐💻

## 📦 依存ライブラリ

私たちのプロジェクトは、以下のライブラリに依存しており、開発環境を簡単に構築できます：

1. **requests** - シンプルなHTTPリクエストライブラリ。
2. **openai** - OpenAI APIと対話するためのライブラリ。
3. **GitPython** - Pythonを使ってGitリポジトリを操作するライブラリ。

依存ライブラリをインストールするには、以下のコマンドを実行するだけです：

```bash
pip install -r requirements.txt
```

## ⚙️ 機能概要

スクリプト `tool.py` は強力な機能を提供します：

1. **設定読み込み** - 設定ファイルからプロジェクトのパラメータを読み取ります。
2. **リポジトリインタラクション** - GitHub APIを通じてリポジトリファイルやその内容を取得します。
3. **内容要約** - OpenAIのAPIを利用してリポジトリファイルの内容を要約し、簡潔な説明を生成します。
4. **README 生成** - ファイル構造と要約情報に基づいてプロフェッショナルな README ファイルを生成します。
5. **翻訳** - README の内容を多言語に翻訳し、活気のある絵文字とスタイルを保持します。😄🎨
6. **Git 操作** - 更新された README と翻訳ファイルをリポジトリにコミットします。

## 🚀 旅を始めよう

手動で GitHub Actions ワークフローを起動するだけで、数分待つと、素晴らしい README ファイルが自動で生成され、翻訳されます。このすべての素晴らしさを楽しむことができます。✨

### 🌟 ぜひ私たちに星を付けてください！あなたのサポートが私たちを前進させる原動力です！💖

ご注目とご支援に感謝します！何か質問や提案があれば、ぜひ GitHub で私たちに連絡してください。より良いオープンソースコミュニティを共に創造できることを楽しみにしています！🤝