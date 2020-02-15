from django.forms import ModelForm
from .models import Feedback


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['author_email', 'text']
        labels = {
            'author_email': 'Your email',
            'text': 'Your feedback'
        }
