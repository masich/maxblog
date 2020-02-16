from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.db.models import Q
from django.utils import timezone
from .models import Post
from .forms import CommentForm, PostForm


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment_set.order_by('id')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'posts/post_details.html', {'post': post, 'comments': comments, 'form': form})


class SearchPostsView(ListView):
    model = Post
    template_name = 'posts/post_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        author = self.request.GET.get('author')
        tag = self.request.GET.get('tag')
        section = self.request.GET.get('section')

        object_list = Post.objects.order_by('-created_date')

        if query:
            object_list = object_list.filter(
                Q(title__icontains=query) | Q(authors__username__icontains=query))
        if author:
            object_list = object_list.filter(
                Q(authors__username__icontains=author))
        if tag:
            object_list = object_list.filter(
                Q(tags__name__icontains=tag))
        if section:
            object_list = object_list.filter(
                Q(section__name__icontains=section))

        return object_list


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('posts:post_details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'posts/post_new.html', {'form': form})
