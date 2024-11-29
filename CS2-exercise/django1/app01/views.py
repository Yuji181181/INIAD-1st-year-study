from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def root(request):
    return HttpResponse('Hello Django')

def pattern(request, username):
    return HttpResponse('Hello {}'.format(username))

def param(request):
    text = ''
    for key in request.GET:
        text += '{} : {}, '.format(key, request.GET[key])
    return HttpResponse(text)

