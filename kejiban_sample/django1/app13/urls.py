# app13/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("thread/<int:pk>/", views.thread_detail, name="thread_detail"),
    path("create/", views.thread_create, name="thread_create"),
    path("edit/<int:pk>/", views.thread_edit, name="thread_edit"),
    path("delete/<int:pk>/", views.thread_delete, name="thread_delete"),
    path("comment/<int:pk>/", views.comment_create, name="comment_create"),
    path("comment/edit/<int:pk>/", views.comment_edit, name="comment_edit"),
    path("comment/delete/<int:pk>/", views.comment_delete, name="comment_delete"),
    path("like/<int:pk>/", views.like_thread, name="like_thread"),
    path("search/", views.search_thread, name="search_thread"),
]
