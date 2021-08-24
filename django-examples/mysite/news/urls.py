from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView,DetailView
from .models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by("-date")[:20],
    template_name="news/posts.html")),
    path('^(?P<pk>\d+)', DetailView.as_view(model=Articles,template_name="news/post.html"))
]
