- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Cambiar idioma: Español](/README/README_Español.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)

# プロジェクト名

私たちのプロジェクトへようこそ！✨ このプロジェクトは、GitHub リポジトリの README ファイルを自動生成および翻訳し、詳細な文書サポートを提供することを目的としています。それでは、プロジェクトの構造と各ファイルの詳細な紹介を見ていきましょう！

## プロジェクト構造

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/main.yml": "main.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "config.json": "config.json",
  "requirements.txt": "requirements.txt",
  "tool.py": "tool.py"
}
```

### ファイルの詳細紹介

#### `.github/workflows/main.yml`
これは、GitHub Actions のワークフローを定義する重要なファイルです。名前は「自動生成と翻訳 README」。🔄 
`workflow_dispatch` イベントを手動でトリガーすることで、このワークフローを開始できます。このワークフローには「build」というタスクが含まれており、Ubuntu 環境で実行されます。このワークフローの目的は、README ファイルの生成と翻訳を自動化し、手動での更新の手間を省くことです。

#### `LICENSE`
このファイルは、Apache ライセンスのバージョン 2.0 の完全なテキストを含んでおり、ソフトウェアとその派生作品の使用、複製、配布の条件を概説しています。🛡️ 
このライセンスはユーザーに、ライセンスによって保護されている作品を修正、使用、配布するための幅広い権利を提供し、いくつかの義務も定めています。このライセンスを通じて、オープンな協力と知的財産の共有を促進したいと考えています。

#### `README.md`
これはプロジェクトの主要な README ファイルで、ユーザーにプロジェクトの概要、使用方法、その他の重要な情報を提供します。📊 
ここでは、プロジェクトのすべての重要情報をまとめて、ユーザーが迅速に始められるようお手伝いします！

#### `README` フォルダ
- `README/README_Deutsch.md`: ドイツ語訳。
- `README/README_English.md`: 英語訳。
- `README/README_Español.md`: スペイン語訳。
- `README/README_Français.md`: フランス語訳。
- `README/README_日本語.md`: 日本語訳。
- `README/README_繁体中文.md`: 繁体字中国語訳。

このフォルダには、プロジェクトの README の多言語版が含まれており、世界中のユーザーがプロジェクトを簡単に理解し、使用できるようにしています。🌍📚

#### `config.json`
このファイルは、自動生成および翻訳 README ドキュメントツールの設定ファイルです。🔧 
リポジトリ名、所有者、API アクセスの基本 URL、使用されるメインブランチ、およびサポートされる翻訳言語などのパラメータが含まれています。設定の目的は、プロジェクト文書のローカライズと翻訳プロセスを簡素化することです。

#### `requirements.txt`
これは標準的な Python プロジェクトの依存ライブラリのリストで、開発環境がプロジェクトに必要な外部ライブラリや依存関係を円滑に実行できるようにします。📦 
これには次のものが含まれます：
1. **requests**: ウェブサービスや REST API と簡単にやり取りするためのライブラリ。
2. **openai**: OpenAI API へのアクセスを提供するライブラリで、自然言語処理や機械学習タスクをサポートします。
3. **GitPython**: ユーザーがプログラミングを通じて Git リポジトリと対話できるようにするライブラリ。

#### `tool.py`
これは、GitHub リポジトリの README ファイルを自動生成および更新するための Python スクリプトです。🤖 
その主な機能は次のとおりです：
- 設定パラメータを読み込む。
- GitHub リポジトリと対話し、ファイル構造と内容を抽出する。
- OpenAI API を利用してファイルの要約を生成する。
- 生成された要約と構造を編纂して、プロフェッショナルな README ファイルを構築する。
- README 内容を多言語に翻訳し、可用性を向上させる。
- README と翻訳ファイルを更新し、変更を GitHub にコミットする。

### 📢 さあ、始めましょう！
このプロジェクトが役に立ったと感じたら、ぜひ ⭐️ してください！すべての Star は私たちの仕事への評価です！ご支援ありがとうございます。一緒にオープンソースの進歩を推進しましょう！🚀

---

ご質問や提案がある場合は、いつでもお気軽にお問い合わせください！皆さまの貴重なご意見をお待ちしています！❤️