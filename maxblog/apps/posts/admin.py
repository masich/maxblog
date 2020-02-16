from django.contrib import admin
from .models import PostAuthor, Post, Comment, Tag, Section


# Register models to be available through admin panel

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Section)
admin.site.register(PostAuthor)
