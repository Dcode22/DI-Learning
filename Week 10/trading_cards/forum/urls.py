from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name="forum"),
    path('thread/<int:thread_id>/', views.thread, name="thread"),
    path('addthread/', views.addThread, name="add_thread"),
    path('addpost/<int:thread_id>/', views.addPost, name="add_post"),
    path('addresponse/<int:post_id>/', views.addResponse, name="add_response")
]