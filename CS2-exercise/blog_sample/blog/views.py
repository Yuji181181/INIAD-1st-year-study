from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')

def update(request, article_id):
	return HttpResponse("article_id: {}".format(article_id))

def hello(request):
	great_message_list = ["Great Fortune", "Small Fortune", "Bad Fortune"]
	random_number = random.randint(0, 2)
	data = {
		'name': 'Alice',
		'weather': 'CLOUDY',
		'weather_detail':['Temperature:23℃','Humidity:40%','Wind: 5m/s'],
		'isGreatFortune':random_number == 0,
		'fortune': great_message_list[random_number]
	}
	return render(request, 'blog/hello.html',data)