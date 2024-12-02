from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('<int:article_id>/update', views.update, name='update'),
    path('hello', views.hello, name='hello'),
]