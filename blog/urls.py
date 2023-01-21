from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("blog/", views.PostList.as_view(), name="blogpost"),
    path("blog/<int:pk>/", views.PostDetail.as_view(), name="post_detail"),
    path("blog/add_post", views.PostCreate.as_view(), name="post_create"),
    path("blog/edit/<slug:slug>/", views.PostUpdate.as_view(), name="post_update"),
    path("blog/<slug:slug>/remove", views.PostDelete.as_view(), name="post_delete"),
    path("blog/like/<int:pk>", views.likeView, name="post_like"),
    path("blog/unlike/<int:pk>", views.unlikeView, name="post_unlike"),
]
