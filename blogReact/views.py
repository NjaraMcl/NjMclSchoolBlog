from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Post
from django.http import JsonResponse


def PostList(request):
    if request.method == "GET":
        post = Post.objects.filter(status=1).order_by("-created_on")
        return JsonResponse(post, safe=False)


def PostDetail(request, pk):
    if request.method == "GET":
        postdetail = get_object_or_404(Post, pk=pk)
        return JsonResponse(postdetail, safe=False)
