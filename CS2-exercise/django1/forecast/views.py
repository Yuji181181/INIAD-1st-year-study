from django.shortcuts import render

# Create your views here.

def index(request):
    params = {}
    params['title'] = '3 days forecast'
    return render(request, 'forecast/index.html', params)