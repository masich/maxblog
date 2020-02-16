from django.db import models
from django.template.defaultfilters import truncatechars

class Feedback(models.Model):
    author_email = models.EmailField()
    text = models.TextField()

    @property
    def short_text(self):
        return truncatechars(self.text, 100)

    def __str__(self):
        return self.text