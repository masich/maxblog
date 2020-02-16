from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.db.models import Q
from .models import Post
from .forms import CommentForm


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
        tag = self.request.GET.get('tag')
        author = self.request.GET.get('author')
        section = self.request.GET.get('section')

        object_list = Post.objects.order_by('-created_date')

        if query:
            object_list = Post.objects.filter(
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
