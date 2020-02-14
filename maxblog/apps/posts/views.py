from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'posts/post_list.html', {'posts': posts})


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.order_by('-id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'posts/post_details.html', {'post': post, 'comments': comments, 'form': form})
