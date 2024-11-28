from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'blog/index.html')

def update(request, article_id):
	return HttpResponse("article_id: {}".format(article_id))