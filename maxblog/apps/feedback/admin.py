from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('author_email', 'short_text',)


admin.site.register(Feedback, FeedbackAdmin)
