## 9-e Djangoアプリケーション作成 初期設定手順


---

### 1. アプリケーションの作成


1.  **アプリケーション作成コマンド実行:**
    - 以下のコマンドをPowerShellで実行し、アプリケーションを作成します。
      ```python
      python manage.py startapp app01
      ```

    - このコマンドにより、アプリケーションディレクトリ `app01` と内部ファイルが作成されます。


### 2. djangoプロジェクトの作成

1.  **プロジェクト作成コマンド実行:**
    - Djangoをインストールした仮想環境が有効な状態で、以下のコマンドをPowerShellで実行し、現在のディレクトリにDjangoプロジェクトを作成します。
      ```python
      django-admin startproject config ./
      ```
      -  `config` のあとに半角スペースとドットスラッシュ (`./`) を忘れずに入力してください。
    - このコマンドにより、 `manage.py` とプロジェクト名のディレクトリ `config` が作成されます。

2.  **VSCodeでプロジェクトフォルダを開く:**
    -  VSCodeで `django1` フォルダを開きます。PowerShellで `django1` ディレクトリに移動後、 `code .` コマンドを実行します。

### 3. settings.py へのアプリケーションの登録

1.  **`settings.py` を編集:**
    - `config/settings.py` を開き、作成したアプリケーション `app01` を登録します。
    - `INSTALLED_APPS` のリストに `'app01'` を追加します。
      ```python
      INSTALLED_APPS = [
          'django.contrib.admin',
          'django.contrib.auth',
          'django.contrib.contenttypes',
          'django.contrib.sessions',
          'django.contrib.messages',
          'django.contrib.staticfiles',
          'app01', # ←  app01 を追加
      ]
      ```

### 4. settings.py の変更

1.  **`settings.py` を編集:**
    - `config/settings.py` を開き、以下の箇所を編集します。
      ```python
      # Internationalization
      # https://docs.djangoproject.com/en/3.1/topics/i18n/

      LANGUAGE_CODE = 'ja'  # 日本語設定
      TIME_ZONE = 'Asia/Tokyo' # タイムゾーンを東京に設定

      USE_I18N = True

      USE_L10N = True

      USE_TZ = True
      ```

### 5. views.py の実装

1.  **`views.py` を編集:**
    - `app01/views.py` を開き、リクエストがあった際に `'Hello Django'` という文字列を返す関数 `root` を追加します。
    - 関数はリクエストを引数として受け取り、戻り値としてレスポンスを返します。
      ```python
      from django.shortcuts import render
      from django.http import HttpResponse

      # Create your views here.
      def root(request):
          return HttpResponse('Hello Django')
      ```

### 6. project の urls.py の実装

1.  **`urls.py` を編集:**
    - `config/urls.py` を開き、作成した関数 `root` とURLをマッピングします。
    - `urlpatterns` リストに `path()` 関数を追加します。
      - `path()` 関数の第一引数がURL、第二引数が関数です。
      - マッピングしたURLへのリクエストが来ると、対応する関数が呼ばれます。
      ```python
      from django.contrib import admin
      from django.urls import path
      import app01.views # app01/views.py をインポート

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('top/', app01.views.root), # 'top/' URL に app01.views.root 関数をマッピング
      ]
      ```
