from django.urls import path
from . import views

app_name = "blogReact"

urlpatterns = [
    path("index/", views.PostList, name="ReactIndex"),
    path("list/", views.PostList, name="ReactPostList"),
    path("<int:pk>", views.PostDetail, name="ReactPostDetail"),
]
