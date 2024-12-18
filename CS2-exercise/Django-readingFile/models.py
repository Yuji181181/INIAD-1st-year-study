from django.db import models  # Djangoのデータベース関連機能をインポート
from django.utils import timezone  # タイムゾーン関連のユーティリティをインポート


# Create your models here.
class Article(models.Model):  # Articleモデルを定義（データベースのテーブルに対応）
    title = models.CharField(
        max_length=200
    )  # 記事のタイトルを格納するCharField（最大200文字）
    body = models.TextField()  # 記事の本文を格納するTextField（テキスト長に制限なし）
    posted_at = models.DateTimeField(
        default=timezone.now
    )  # 記事の投稿日時を格納するDateTimeField（デフォルトは現在時刻）
    published_at = models.DateTimeField(
        blank=True, null=True
    )  # 記事の公開日時を格納するDateTimeField（空でも可、nullでも可）
    like = models.IntegerField(
        default=0
    )  # 記事のいいね数を格納するIntegerField（デフォルトは0）

    def publish(self):  # 記事を公開するメソッド
        self.published_at = timezone.now()  # 公開日時を現在時刻に設定
        self.save()  # 変更をデータベースに保存

    def __str__(self):  # モデルの文字列表現を定義
        return self.title  # オブジェクトを文字列として表現するときにタイトルを返す


class Comment(models.Model):  # Commentモデルを定義（データベースのテーブルに対応）
    text = (
        models.TextField()
    )  # コメントの本文を格納するTextField（テキスト長に制限なし）
    posted_at = models.DateTimeField(
        default=timezone.now
    )  # コメントの投稿日時を格納するDateTimeField（デフォルトは現在時刻）
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )  # コメントが関連付けられる記事へのForeignKey（Articleモデルとの多対一の関係、関連名を'comments'とする、記事が削除されたらコメントも削除する）
