from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Thread, Comment
from django.http import HttpResponse
from django.db.models import Q
from datetime import datetime, timedelta


def index(request):
    sort_by = request.GET.get("sort", "likes")
    search_query = request.GET.get("search", "")
    threads = Thread.objects.all()
    if sort_by == "likes":
        threads = threads.order_by("-likes")
    elif sort_by == "created_at":
        threads = threads.order_by("-created_at")
    if search_query:
        threads = threads.filter(Q(title__icontains=search_query))
    return render(
        request,
        "app13/index.html",
        {"threads": threads, "search_query": search_query, "sort_by": sort_by},
    )


def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    return render(request, "app13/detail.html", {"thread": thread})


def thread_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Thread.objects.create(title=title, content=content)
        return redirect("index")
    return render(request, "app13/form.html")


def thread_edit(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == "POST":
        thread.title = request.POST.get("title")
        thread.content = request.POST.get("content")
        thread.save()
        return redirect("thread_detail", pk=thread.pk)
    return render(request, "app13/form.html", {"thread": thread})


def thread_delete(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    thread.delete()
    return redirect("index")


def comment_create(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == "POST":
        text = request.POST.get("text")
        Comment.objects.create(thread=thread, text=text)
        return redirect("thread_detail", pk=thread.pk)
    return HttpResponse("コメントの送信に失敗しました")


def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    thread_pk = comment.thread.pk
    if request.method == "POST":
        comment.text = request.POST.get("text")
        comment.edited_at = timezone.now()
        comment.save()
        return redirect("thread_detail", pk=thread_pk)
    return render(request, "app13/comment_form.html", {"comment": comment})


def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    thread_pk = comment.thread.pk
    comment.delete()
    return redirect("thread_detail", pk=thread_pk)


def like_thread(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    thread.likes += 1
    thread.save()
    return redirect("index")


def search_thread(request):
    search_query = request.GET.get("search", "")
    threads = Thread.objects.filter(Q(title__icontains=search_query))
    return render(
        request, "app13/index.html", {"threads": threads, "search_query": search_query}
    )


def time_ago(time):
    now = timezone.now()
    diff = now - time
    if diff < timedelta(minutes=1):
        return "1分未満"
    elif diff < timedelta(hours=1):
        return f"{diff.seconds // 60}分前"
    elif diff < timedelta(days=1):
        return f"{diff.seconds // 3600}時間前"
    else:
        return f"{diff.days}日前"
