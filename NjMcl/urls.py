from NjMcl import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("", include("blog.urls", namespace="blog")),
    path("api/", include("blog_api.urls", namespace="blog_api")),
    path("blogReact/", include("blogReact.urls", namespace="blog_react")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
