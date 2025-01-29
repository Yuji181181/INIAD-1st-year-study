# Djangoテンプレート言語の基本構文

## 変数の表示
テンプレート内で変数を表示するには、二重中括弧 `{{ }}` を使用します。
```html
{{ 変数名 }}
```
## 属性の表示
変数の属性を表示するには、ドット . を使用します。
```html
{{ 変数名.属性名 }}
```

## フィルターの使用
フィルターを使用して変数の値を変換できます。フィルターはパイプ | で指定します。
```html
{{ 変数名 | フィルタ名 }}
```

## forループ
リストの各要素に対してループを実行するには、{% for %} タグを使用します。
```html
{% for 変数名 in リスト %}
    <!-- ループ内の処理 -->
{% endfor %}
```

## if文
条件分岐を行うには、{% if %} タグを使用します。
```html
{% if 変数 %}
    <!-- 条件が真の場合の処理 -->
{% else %}
    <!-- 条件が偽の場合の処理 -->
{% endif %}
```
## URLの逆引き
URLの逆引きを行うには、{% url %} タグを使用します。
```html
{% url '名前' 変数,変数... %}
```

## 静的ファイルの読み込み
静的ファイルをテンプレートに含めるには、{% load static %} タグを使用します。
```html
{% load static %}
```

## 静的ファイルのパス
静的ファイルのパスを取得するには、{% static %} タグを使用します。
```html
{% static 'パス' %}
```

## CSRFトークン
フォームにCSRFトークンを含めるには、{% csrf_token %} タグを使用します。
```html
{% csrf_token %}
```
![alt text](image/image-15.png)
![alt text](image/image-16.png)
![alt text](image/image-17.png)
![alt text](image/image-18.png)
![alt text](image/image-19.png)
![alt text](image/image-20.png)
![alt text](image/image-21.png)
![alt text](image/image-22.png)
![alt text](image/image-23.png)
![alt text](image/image-24.png)
![alt text](image/image-25.png)
![alt text](image/image-26.png)
![alt text](image/image-27.png)
![alt text](image/image-28.png)
![alt text](image/image-29.png)
![alt text](image/image-30.png)
![alt text](image/image-31.png)
![alt text](image/image-32.png)
![alt text](image/image-33.png)
![alt text](image/image-34.png)
![alt text](image/image-35.png)