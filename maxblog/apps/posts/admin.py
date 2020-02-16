from django.contrib import admin
from .models import PostAuthor, Post, Comment, Tag, Section


# Register models to be available through admin panel

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_text', 'created_date', 'section',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author_name', 'short_text',)


class PostAuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class SectionAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(PostAuthor, PostAuthorAdmin)
