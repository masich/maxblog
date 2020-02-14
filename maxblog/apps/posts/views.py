from django.shortcuts import render, HttpResponse
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_date')
    return render(request, 'posts/post_list.html', {'posts': posts})
