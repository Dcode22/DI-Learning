from django.shortcuts import render, redirect
from django.http import request
from .models import *
from .forms import *

# Create your views here.

def forum(request):
    return render(request, "forum_home.html")


def thread(request, thread_id):
    return render(request, "thread.html", {'thread': Thread.objects.get(id=thread_id)})


def addThread(request):
    form = ThreadCreateForm(request.user)
    if request.method =="POST":
        if form.is_valid:
            Thread.objects.create()
        else:
            return render(request, "add_thread.html", {'form': form})
    if request.method == "GET":
        return render(request, "add_thread.html", {'form': form})

def addPost(request, thread_id):
    thread = Thread.objects.get(id=thread_id)
    form = PostCreateForm(request.user)
    if request.method =="POST":
        if form.is_valid:
            Post.objects.create()
        else:
            return render(request, "add_post.html", {'form': form, 'thread': thread})
    if request.method == "GET":
        return render(request, "add_post.html", {'form': form, 'thread': thread})



def addResponse(request, post_id):
    post = Post.objects.get(id=post_id)
    form = ResponseCreateForm(request.user)
    if form.method =="POST":
        if form.is_valid:
            Response.objects.create()
        else:
            return render(request, "add_response.html", {'form': form, 'post': post})
    if form.method == "GET":
        return render(request, "add_response.html", {'form': form, 'post': post})



