from django.urls import path
from . import views

app_name = "blogReact"

urlpatterns = [
    path("<int:pk>", views.PostDetail, name="ReactPostDetail"),
    path("", views.PostList, name="ReactPostList"),
]
