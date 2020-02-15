from django.forms import forms, ModelForm

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author_name', 'text']
        labels = {
            'author_name': 'Your name',
            'text': 'Comment'
        }
