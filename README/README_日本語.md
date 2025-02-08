- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)

# README - 自動生成と翻訳ツール 🌟

**README-Automatic-Generation-and-Translation-Tool** プロジェクトへようこそ！🚀

私たちは、開発者がGitHubプロジェクトのREADMEファイルを簡単に生成・翻訳できる自動化ツールを提供することに力を入れています。あなたのプロジェクト文書をより魅力的でプロフェッショナルにしましょう！💕 

## プロジェクト構成 📂

以下は現在のプロジェクトの構成で、各ファイルの説明は次の通りです：

```
├── .github
│   └── workflows
│       └── main.yml     # GitHub Actionsのワークフロー設定ファイル
├── LICENSE                # プロジェクトのライセンスファイル
├── README.md              # プロジェクトの主要文書
├── README
│   ├── README_Deutsch.md  # ドイツ語のREADMEファイル
│   ├── README_English.md  # 英語のREADMEファイル
│   ├── README_Español.md  # スペイン語のREADMEファイル
│   ├── README_Français.md # フランス語のREADMEファイル
│   ├── README_日本語.md    # 日本語のREADMEファイル
│   └── README_繁体中文.md   # 繁体字中国語のREADMEファイル
├── config.json            # プロジェクトの設定ファイル
├── requirements.txt       # Pythonの依存ライブラリリスト
└── tool.py                # READMEファイルを自動生成および更新するスクリプト
```

## ファイル概要 📄

### 1. `.github/workflows/main.yml`
このGitHub Actionsのワークフロー設定ファイルは、READMEファイルの生成と翻訳を自動化することに役立ちます。最新のUbuntu環境で実行され、以下の手順を行います：

- **コードのチェックアウト**：最新のコードを取得します。
- **Pythonの設定**：環境としてPython 3.8を設定します。
- **依存関係のインストール**：pipをアップグレードし、必要なPythonパッケージ（requests、openai、GitPython）をインストールします。
- **スクリプトの実行**：Pythonスクリプト（tool.py）を実行し、GitHubとOpenAI APIの認証情報を使用してREADMEを生成します。

### 2. `LICENSE`
このファイルはApache License Version 2.0を含んでおり、ソフトウェアやその他の作品の使用、コピー、配布の条件を概説しています。このライセンスは、オープンソースソフトウェアの開発を促進し、寄稿者とユーザーの権利を保護する法的フレームワークを提供します。

### 3. `config.json`
この設定ファイルは、プロジェクトの重要なパラメータを定義しています。例えば：リポジトリ名、オーナー、基本API URL、およびデフォルトブランチ（main）などです。READMEファイルの自動生成と翻訳をサポートします。

### 4. `requirements.txt`
Pythonプロジェクトに必要な依存ライブラリをリストアップしています：

- **requests**：HTTPリクエストを簡素化する人気ライブラリです。
- **openai**：OpenAI APIと対話するためのライブラリです。
- **GitPython**：Pythonから直接Gitリポジトリを操作・対話するためのライブラリです。

### 5. `tool.py`
このスクリプトは、GitHubリポジトリ内のREADMEファイルとその翻訳を自動的に生成および更新します。主な機能は次の通りです：

1. **設定と準備**：設定をロードし、必要な環境変数を取得します。
2. **ファイル管理**：GitHubリポジトリにアクセスし、ファイル構成と内容を取得します。
3. **README生成**：OpenAIのAPIを利用して詳細なREADMEファイルを生成します。
4. **翻訳作成**：生成されたREADMEを複数の言語に翻訳します。
5. **リンクと構造の統合**：ナビゲーションの向上を図ります。
6. **コミットとプッシュ**：更新されたファイルをGitHubリポジトリにコミットします。

## クイックスタート 🚀

参加したいですか？右上の⭐をクリックして、私たちのプロジェクトに投票してください！ 💖 

このツールを通じて、すべての開発者がプロジェクト文書を簡単に維持でき、プロジェクトの国際化を進める手助けをしています！大きなプロジェクトでも小さなプロジェクトでも、文書に関する心配を取り除き、より良いオープンソースエコシステムを一緒に作り上げましょう！🌍👩‍💻👨‍💻

質問や提案がある場合は、いつでもご連絡ください！ハッピーコーディング！🎉