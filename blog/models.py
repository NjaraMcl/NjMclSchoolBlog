from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=1)

    STATUS = ((0, "Draft"), (1, "Publish"))
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique_for_date="created_on")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name="blogposts_likes")
    unlikes = models.ManyToManyField(User, related_name="blogposts_unlikes")
    status = models.IntegerField(choices=STATUS, default=0)
    objects = models.Manager()  # Default Manager
    postobjects = PostObjects()  # Custom PostObjects

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
