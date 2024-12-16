from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
import random
from django.utils import timezone
from blog.models import Article


# Create your views here.
def index(request):
    context = {"articles": Article.objects.all()}
    return render(request, "blog/index.html", context)


def detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")
    context = {"article": article}
    return render(request, "blog/detail.html", context)


def update(request, article_id):
    context = {"article_id": article_id}
    return render(request, "blog/tbd.html", context)


def delete(request, article_id):
    return redirect(index)


def hello(request):
    great_message_list = ["Great Fortune", "Small Fortune", "Bad Fortune"]
    random_number = random.randint(0, 2)
    data = {
        "name": "Alice",
        "weather": "CLOUDY",
        "weather_detail": ["Temperature:23℃", "Humidity:40%", "Wind: 5m/s"],
        "isGreatFortune": random_number == 0,
        "fortune": great_message_list[random_number],
    }
    return render(request, "blog/hello.html", data)


def redirect_test(request):
    return redirect(hello)
