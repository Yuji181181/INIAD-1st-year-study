## 9-1 ウェブ開発と Django によるシステム開発

このドキュメントは、9-1 ウェブ開発の基礎と Django フレームワークを用いたウェブ開発の内容をまとめたものである。

### 1. Web サービスのアーキテクチャ（スライド１）

- **Web サービス:** インターネット上で提供される多様なサービスの総称だ。検索エンジン、ソーシャルネットワーキングサービス (SNS)、電子商取引 (EC) サイト、オンラインバンキングなどが該当する。ユーザーはウェブブラウザを介してこれらのサービスにアクセスし、機能を利用する。
- **クライアント・サーバーモデル:** Web サービスを支える基盤となるアーキテクチャだ。クライアント (ユーザーの端末・ウェブブラウザ) がサーバーに対してリクエスト (要求) を送信し、サーバーはそれに応じたレスポンス (応答) を返却する。この一連のやり取りによって、Web サービスが成り立つ。
- **Web ブラウザ:** クライアント側のソフトウェアであり、ユーザーが Web ページを閲覧するために使用するものだ。HTML、CSS、JavaScript を解釈し、Web ページを適切に表示する。主要な Web ブラウザとしては、Google Chrome、Mozilla Firefox、Apple Safari、Microsoft Edge などが挙げられる。
- **Web サーバー:** サーバー側のソフトウェアであり、クライアントからのリクエストを受け、Web ページのデータや画像などのリソースを提供する。代表的な Web サーバーとしては、Apache HTTP Server、Nginx などが挙げられる。
- **HTTP/HTTPS:** Web で使用される通信プロトコルだ。HTTP (HyperText Transfer Protocol) は、Web ページの送受信に用いられる標準的なプロトコルである。HTTPS (HyperText Transfer Protocol Secure) は、HTTP にセキュリティ機能 (SSL/TLS) を追加したもので、通信内容を暗号化することで安全なデータ送受信を実現する。
- **URL (Uniform Resource Locator):** Web ページのアドレスであり、Web サーバー上のリソースを一意に識別する。`https://www.example.com/index.html` のように、プロトコル、ドメイン名、パスなどで構成される。
- **HTML (HyperText Markup Language):** Web ページの構造を記述するためのマークアップ言語だ。テキスト、画像、リンクなどを配置するためのタグを用いて記述する。
- **CSS (Cascading Style Sheets):** Web ページのスタイル (見た目) を記述するためのスタイルシート言語だ。HTML 要素の色、フォント、レイアウトなどを指定する。
- **JavaScript:** Web ページに動的な機能を追加するためのプログラミング言語だ。ユーザーの操作に応じて Web ページの内容を動的に変更したり、アニメーションを表示したりできる。

### 2. Web アプリケーションとフレームワーク（スライド２）

- **Web アプリケーション:** Web ブラウザ上で動作するアプリケーションだ。ユーザーは Web ブラウザを通じてサーバーと対話し、様々な機能を利用できる。
- **Web フレームワーク:** Web アプリケーション開発を効率化するためのソフトウェアフレームワークだ。複雑な処理を簡略化し、開発速度の向上に貢献する。セキュリティ対策やデータベースとの連携機能なども提供する。
- **Web フレームワークの利点:** 開発効率の向上、セキュリティの向上、メンテナンス性の向上、チーム開発の効率化などが挙げられる。
- **代表的な Web フレームワーク:** Ruby (Ruby on Rails)、Python (Django, Flask, FastAPI, Pyramid)、Java (Spring, Struts)、JavaScript (Node.js, React, Vue.js, Angular)、PHP (Laravel, Symfony) など、様々なプログラミング言語で実装されたフレームワークが存在する。
- **MVC (Model-View-Controller):** Web アプリケーションの設計パターンの一つだ。アプリケーションを Model (データ), View (表示), Controller (処理) の 3 つの要素に分割することで、コードの整理、再利用性、保守性の向上を実現する。
  - **Model:** データベースへのアクセスやデータの操作を担当する。
  - **View:** ユーザーインターフェース (UI) の表示を担当する。HTML などを生成する。
  - **Controller:** ユーザーからのリクエストを受け取り、Model と View を連携させて処理を実行する。
- **Django:** Python で実装された Web フレームワークだ。MVC アーキテクチャを採用しており、高速で安全な Web アプリケーション開発を可能にする。豊富な機能と活発なコミュニティによって支えられており、多くの開発者に利用されている。Object-Relational Mapper (ORM) を搭載しており、データベース操作を Python コードで記述できる。

### 3. 開発環境構築（スライド３）

- **Python のインストール:** Python 公式サイトから適切なバージョンのインストララーをダウンロードし、インストールする。
- **仮想環境の作成:** `venv` モジュールを使用して仮想環境を作成する。仮想環境はプロジェクトごとに独立した Python 環境を提供し、ライブラリのバージョン競合などを防ぐ。
  - `python -m venv .venv` (Windows)
  - `python3 -m venv .venv` (macOS/Linux)
- **Django のインストール:** `pip` コマンドを使用して Django をインストールする。仮想環境をアクティベートした状態で `pip install django` を実行する。

### 4. プロジェクト作成（スライド４）

**Windows:**

1. コマンドプロンプトまたは PowerShell を管理者権限で実行する。
2. プロジェクト用のディレクトリを作成し、cd コマンドで移動する。例: `mkdir myproject` & `cd myproject`
3. 仮想環境の作成: `python -m venv .venv`
4. 仮想環境の有効化: `.venv\Scripts\activate`
5. Django のインストール: `pip install django`
6. プロジェクトの作成: `django-admin startproject myproject .` (`.` はカレントディレクトリ指定)
7. アプリケーションの作成: プロジェクトディレクトリに移動後、`python manage.py startapp myapp`
8. データベースのマイグレーション: `python manage.py migrate`
   - **注意**：models.py を編集した場合は、`python manage.py makemigration` コマンドを実行してマイグレーションファイルを生成する必要がこのコマンドの実行前にある。
9. 開発サーバーの起動: `python manage.py runserver`

**macOS/Linux:**

1. ターミナルを開く。
2. プロジェクト用のディレクトリを作成し、cd コマンドで移動する。例: `mkdir myproject` & `cd myproject`
3. 仮想環境の作成: `python3 -m venv .venv` (macOS/Linux では`python3`を使用)
4. 仮想環境の有効化: `source .venv/bin/activate`
5. Django のインストール: `pip install django`
6. プロジェクトの作成: `django-admin startproject myproject .` (`.` はカレントディレクトリ指定)
7. アプリケーションの作成: プロジェクトディレクトリに移動後、`python manage.py startapp myapp`
8. データベースのマイグレーション: `python manage.py migrate`
9. 開発サーバーの起動: `python manage.py runserver`
