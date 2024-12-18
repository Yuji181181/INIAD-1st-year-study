from django.shortcuts import (
    render,
    redirect,
)  # Djangoのショートカット関数（レンダリング、リダイレクト）をインポート
from django.http import (
    HttpResponse,
)  # HTTPレスポンスを返すためのHttpResponseをインポート
from django.http import (
    Http404,
    JsonResponse,
)  # 404エラーを発生させるHttp404、JSONレスポンスを返すJsonResponseをインポート
from django.utils import timezone  # タイムゾーン関連のユーティリティをインポート
import random  # 乱数を生成するためのrandomモジュールをインポート
from blog.models import (
    Article,
    Comment,
)  # blogアプリのモデル（記事とコメント）をインポート


# Create your views here.
def index(request):  # ブログのトップページを表示するビュー関数
    if request.method == "POST":  # リクエストがPOSTメソッドの場合
        article = Article(
            title=request.POST["title"], body=request.POST["text"]
        )  # フォームデータから新しい記事オブジェクトを作成
        article.save()  # 記事をデータベースに保存
        return redirect(detail, article.id)  # 作成した記事の詳細ページにリダイレクト

    if "sort" in request.GET:  # GETパラメータに'sort'が含まれているか確認
        if request.GET["sort"] == "like":  # 'sort'パラメータの値が'like'の場合
            articles = Article.objects.order_by("-like")  # 記事をいいね数が多い順に取得
        else:  # それ以外の場合
            articles = Article.objects.order_by(
                "-posted_at"
            )  # 記事を投稿日時が新しい順に取得
    else:  # GETパラメータに'sort'が含まれていない場合
        articles = Article.objects.order_by(
            "-posted_at"
        )  # 記事を投稿日時が新しい順に取得

    context = {  # テンプレートに渡すデータを辞書に格納
        "articles": articles  # 取得した記事リストを'articles'キーで格納
    }

    return render(
        request, "blog/index.html", context
    )  # index.htmlをレンダリングしてレスポンスを返す


def hello(request):  # サンプルページを表示するビュー関数
    messages = [
        "Great Fortune!",
        "Small Fortune",
        "Bad Fortune..",
    ]  # おみくじのメッセージリスト
    fortune = random.randint(0, 2)  # 0から2までの乱数を生成
    isGreatFortune = fortune == 0  # 乱数が0（大吉）かどうかを判定
    fortuneMessage = messages[fortune]  # ランダムに選んだメッセージを取得

    data = {  # テンプレートに渡すデータを辞書に格納
        "name": "Alice",  # 名前
        "weather": "CLOUDY",  # 天気
        "weather_detail": [
            "Temperature: 23℃",
            "Humidity: 40%",
            "Wind: 5m/s",
        ],  # 天気の詳細情報
        "isGreatFortune": isGreatFortune,  # 大吉かどうか
        "fortune": fortuneMessage,  # おみくじの結果
    }
    return render(
        request, "blog/hello.html", data
    )  # hello.htmlをレンダリングしてレスポンスを返す


def redirect_test(request):  # hello関数にリダイレクトするビュー関数
    return redirect(hello)  # hello関数が処理するURLにリダイレクト


def detail(request, article_id):  # 特定の記事詳細ページを表示するビュー関数
    try:  # 例外処理開始
        article = Article.objects.get(
            pk=article_id
        )  # 指定されたIDの記事をデータベースから取得
    except Article.DoesNotExist:  # 記事が見つからない場合
        raise Http404("Article does not exist")  # 404エラーを発生させる

    if request.method == "POST":  # リクエストがPOSTメソッドの場合
        comment = Comment(
            article=article, text=request.POST["text"]
        )  # フォームデータから新しいコメントオブジェクトを作成
        comment.save()  # コメントをデータベースに保存

    context = {  # テンプレートに渡すデータを辞書に格納
        "article": article,  # 取得した記事データを'article'キーで格納
        "comments": article.comments.order_by(
            "-posted_at"
        ),  # 記事のコメントを投稿日時が新しい順に取得し'comments'キーで格納
    }
    return render(
        request, "blog/detail.html", context
    )  # detail.htmlをレンダリングしてレスポンスを返す


def update(request, article_id):  # 特定の記事を編集するビュー関数
    try:  # 例外処理開始
        article = Article.objects.get(
            pk=article_id
        )  # 指定されたIDの記事をデータベースから取得
    except Article.DoesNotExist:  # 記事が見つからない場合
        raise Http404("Article does not exist")  # 404エラーを発生させる
    if request.method == "POST":  # リクエストがPOSTメソッドの場合
        article.title = request.POST["title"]  # フォームデータから記事のタイトルを更新
        article.body = request.POST["text"]  # フォームデータから記事の本文を更新
        article.save()  # 記事をデータベースに保存
        return redirect(detail, article_id)  # 編集した記事の詳細ページにリダイレクト

    context = {  # テンプレートに渡すデータを辞書に格納
        "article": article  # 取得した記事データを'article'キーで格納
    }
    return render(
        request, "blog/edit.html", context
    )  # edit.htmlをレンダリングしてレスポンスを返す


def delete(request, article_id):  # 特定の記事を削除するビュー関数
    try:  # 例外処理開始
        article = Article.objects.get(
            pk=article_id
        )  # 指定されたIDの記事をデータベースから取得
    except Article.DoesNotExist:  # 記事が見つからない場合
        raise Http404("Article does not exist")  # 404エラーを発生させる
    article.delete()  # 記事をデータベースから削除
    return redirect(index)  # 記事一覧ページにリダイレクト


def like(request, article_id):  # 特定の記事のいいね数を増やすビュー関数
    try:  # 例外処理開始
        article = Article.objects.get(
            pk=article_id
        )  # 指定されたIDの記事をデータベースから取得
        article.like += 1  # 記事のいいね数を1増やす
        article.save()  # 記事をデータベースに保存
    except Article.DoesNotExist:  # 記事が見つからない場合
        raise Http404("Article does not exist")  # 404エラーを発生させる

    return redirect(detail, article_id)  # 記事の詳細ページにリダイレクト


def api_like(
    request, article_id
):  # 特定の記事のいいね数を増やしてJSONで返すAPIビュー関数
    try:  # 例外処理開始
        article = Article.objects.get(
            pk=article_id
        )  # 指定されたIDの記事をデータベースから取得
        article.like += 1  # 記事のいいね数を1増やす
        article.save()  # 記事をデータベースに保存
    except Article.DoesNotExist:  # 記事が見つからない場合
        raise Http404("Article does not exist")  # 404エラーを発生させる

    result = {  # JSONレスポンスとして返す辞書を作成
        "id": article_id,  # 記事のID
        "like": article.like,  # 記事のいいね数
    }
    return JsonResponse(result)  # JSONレスポンスを返す
