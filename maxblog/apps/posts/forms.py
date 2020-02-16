from django.forms import forms, ModelForm

from .models import Comment, Post


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        labels = {
            'author_name': 'Your name',
            'text': 'Comment'
        }

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['authors', 'title', 'text', 'tags', 'section']
        labels = {
            'authors': 'Post authors',
            'title': 'Post title',
            'text': 'Post text',
            'tags': 'Post tags',
            'section': 'Post section',
        }
