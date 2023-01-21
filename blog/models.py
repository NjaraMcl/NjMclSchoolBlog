from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()
STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="blogposts_likes")
    unlikes = models.ManyToManyField(User, related_name="blogposts_unlikes")
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_number_of_likes(self):
        return self.likes.count()

    def get_number_of_unlikes(self):
        return self.unlikes.count()

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
