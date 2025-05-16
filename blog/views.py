from django.shortcuts import render, get_object_or_404
from .models import Post
from django.db.models import Q

def home(request):

    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query)
            )
    else:
        posts = Post.objects.all()[:3]

    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def all_posts(request):
    allpost = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'posts': allpost})

