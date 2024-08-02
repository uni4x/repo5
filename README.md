# Markdown表示アプリ

## 概要

Djangoで作成した、シンプルなMarkdown表示アプリです。Markdown形式でノートを作成、編集、削除、表示することができます。

## 機能

* ノートの作成、編集、削除
* ノートの表示 (タイトル、コンテンツ、タグ)
* タグ付け
* プレビュー表示 (MarkdownをHTMLに変換)

## 使用技術

* Python
* Django
* Django REST framework
* HTML
* CSS
* JavaScript
* marked.js

## セットアップ方法

1. Python 3.7以上をインストール
2. 仮想環境を作成
   ```bash
   python -m venv .venv
   ```
3. 仮想環境をアクティベート
   ```bash
   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```
4. 必要なパッケージをインストール
   ```bash
   pip install -r requirements.txt
   ```
5. データベースをマイグレート
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. 開発サーバーを起動
   ```bash
   python manage.py runserver
   ```

## 使い方

1. ブラウザで `http://127.0.0.1:8000/` にアクセス
2. "Create New Note" ボタンをクリックしてノートを作成
3. ノートを編集、削除するには、一覧画面の各ノートの "Edit"、"Delete" ボタンをクリック


## 追記

これはポートフォリオです。