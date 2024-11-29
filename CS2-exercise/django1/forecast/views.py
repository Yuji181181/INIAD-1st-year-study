from django.shortcuts import render
import random

# Create your views here.

weathers = ['Sunny', 'Rainy', 'Cloudy', 'Snowy']
def index(request):
    params = {}
    params['title'] = '3 days forecast'
    params['forecast'] = random.choices(weathers, k=3)
    return render(request, 'forecast/index.html', params)