[Back to main language README](README.md)

# README: 自動生成および翻訳ツール 📄🌍

## プロジェクト紹介 ✨

ようこそ **README-Automatic-Generation-and-Translation-Tool** プロジェクトへ！このツールは、GitHubリポジトリのREADMEファイルの生成と翻訳プロセスを簡素化することを目的としています。GitHub APIとOpenAI APIを組み合わせることで、私たちのツールは包括的なREADMEドキュメントを自動生成し、多言語翻訳をサポートします。これにより、あなたのプロジェクトは世界中のユーザーにとってアクセスしやすく理解しやすくなります。

## 機能特徴 🚀

- **自動化設定管理**：設定ファイルから設定をロードします。
- **GitHub API互換**：指定されたGitHubリポジトリのファイル内容を取得します。
- **OpenAI API統合**：OpenAI APIを使用してファイル内容を要約し、魅力的なREADMEテキストと翻訳を生成します。
- **多言語サポート**：事前定義された言語設定に基づいて翻訳版を生成します。
- **README管理**：プロジェクト概要、インストール手順などの複数の部分を含むREADMEファイルを構築し、翻訳版にリンクします。
- **バージョン管理**：READMEとその翻訳を生成した後、変更を自動的にGitHubリポジトリにコミットしてバージョン管理を維持します。

## インストール手順 ⚙️

このツールを使用する前に、以下の依存関係がインストールされていることを確認してください：

1. **リポジトリをクローン**：
   ```bash
   git clone https://github.com/Delta-Water/README-Automatic-Generation-and-Translation-Tool.git
   cd README-Automatic-Generation-and-Translation-Tool
   ```

2. **依存関係のインストール**：
   `pip`を使用してプロジェクトに必要なライブラリをインストールします：
   ```bash
   pip install -r requirements.txt
   ```

3. **設定ファイル**：プロジェクトのルートディレクトリに`config.json`ファイルを作成または編集し、API URLと他の設定項目を設定します。

4. **GitHubキーの設定**：GitHubの「Secrets」セクションで個人アクセストークンを設定し、ツールがあなたのGitHubリポジトリにアクセスできるようにします。

## 使用方法 📋

1. **設定**：`config.json`ファイルがBase API URL、メインブランチ、および主要プログラミング言語インデックスを正しく設定されていることを確認します。

2. **ツールを実行**：以下のコマンドを実行してツールを起動します：
   ```bash
   python tool.py
   ```

3. **GitHub Actionsを手動でトリガー**：手動でGitHub Actionsを実行することも、新しいコミット時に自動で実行されるように設定することもできます。

## 貢献ガイド 🤝

あらゆる形の貢献を歓迎します！以下の手順に従ってください：
1. **このリポジトリをフォーク**します。
2. **機能ブランチを作成**します：
   ```bash
   git checkout -b feature/MyFeature
   ```
3. **変更をコミット**します：
   ```bash
   git commit -m "Add some feature"
   ```
4. **ブランチにプッシュ**します：
   ```bash
   git push origin feature/MyFeature
   ```
5. **プルリクエストを提出**します。

このプロジェクトへのご支援ありがとうございます！質問や提案がある場合は、問題を作成するか、プロジェクトのメンテナに連絡してください。🙏

## ライセンス 📜

このプロジェクトは **Apache License, Version 2.0** に従います。詳細な条項と条件については関連文書を参照し、協力と使用の合法性と公正性を確保してください。

---

**README-Automatic-Generation-and-Translation-Tool** をご利用いただきありがとうございます！オープンソースをよりオープンで協力的にしていきましょう！💪