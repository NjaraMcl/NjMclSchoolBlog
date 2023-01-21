from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Post
from .forms import addPostForm, editPostForm
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.views import View
from django.core import serializers
import json


def likeView(request, pk):
    if request.method == "POST":
        print(request.POST.get("post_id"))
        post = get_object_or_404(Post, id=pk)
        unliked = post.unlikes.filter(id=request.user.id).exists()
        liked = False
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            liked = False
        else:
            post.likes.add(request.user)
            post.unlikes.remove(request.user)
            liked = True
        data = {
            "likesCount": post.get_number_of_likes(),
            "unlikesCount": post.get_number_of_unlikes(),
            "liked": liked,
            "unliked": unliked,
        }
        return JsonResponse(data, safe=False)
    return HttpResponseRedirect(reverse("blog:post_detail", args=[str(pk)]))


def unlikeView(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, id=pk)
        liked = post.likes.filter(id=request.user.id).exists()
        unliked = False
        if post.unlikes.filter(id=request.user.id).exists():
            post.unlikes.remove(request.user)
            unliked = False
        else:
            post.unlikes.add(request.user)
            post.likes.remove(request.user)
            unliked = True
        data = {
            "likesCount": post.get_number_of_likes(),
            "unlikesCount": post.get_number_of_unlikes(),
            "liked": liked,
            "unliked": unliked,
        }
        return JsonResponse(data, safe=False)
    return HttpResponseRedirect(reverse("blog:post_detail", args=[str(pk)]))


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog/index.html"
    paginate_by = 3


class PostDetail(generic.DetailView):
    template_name = "blog/post_detail.html"

    def get(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs["pk"])
        author = post.author
        author = serializers.serialize("json", [author])
        postdata = serializers.serialize("json", [post])
        if post:
            if post.likes.filter(id=request.user.id).exists():
                liked = True
            else:
                liked = False
            if post.unlikes.filter(id=request.user.id).exists():
                unliked = True
            else:
                unliked = False
        return render(
            request,
            self.template_name,
            {
                "liked": liked,
                "unliked": unliked,
                "total_likes": post.get_number_of_likes(),
                "total_unlikes": post.get_number_of_unlikes(),
                "page_title": post.title,
                "post": post,
                "postdata": json.dumps(postdata),
                "author": json.dumps(author),
            },
        )


class PostCreate(generic.CreateView):
    model = Post
    template_name = "blog/post_create.html"
    form_class = addPostForm


class PostUpdate(generic.UpdateView):
    model = Post
    template_name = "blog/post_update.html"
    form_class = editPostForm


class PostDelete(generic.DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = reverse_lazy("main:home")
