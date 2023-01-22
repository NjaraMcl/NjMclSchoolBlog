from django.shortcuts import render, get_object_or_404
from django.core import serializers
from django.views import generic
from blog.models import Post
from django.http import JsonResponse
import json


def index(request):
    return render(request, "index.html")


def PostList(request):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    json_data = serializers.serialize("json", queryset)
    postData = json.loads(json_data)
    return JsonResponse(postData, content_type="application/json", safe=False)


def PostDetail(request, pk):
    poste = get_object_or_404(Post, pk=pk)
    postdat = serializers.serialize("json", [poste])
    postdetail = json.dumps(postdat)
    return JsonResponse(postdetail, content_type="application/json", safe=False)
