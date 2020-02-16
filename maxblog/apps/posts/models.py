from django.db import models
from django.utils import timezone
from django.conf import settings


class Section(models.Model):
    """
    The topic section to which the Post may relate
    """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostAuthor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    authors = models.ManyToManyField(PostAuthor)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.author_name
