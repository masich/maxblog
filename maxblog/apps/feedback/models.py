from django.db import models


class Feedback(models.Model):
    author_email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.text