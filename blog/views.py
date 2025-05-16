from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from django.db.models import Q
from .forms import CommentForm

def home(request):

    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query))
    else:
        posts = Post.objects.all()[:3]

    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(approved=True)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html',
                   {'post': post,
                    'comments':comments,
                    'form':form
                    })

def all_posts(request):
    allpost = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'posts': allpost})

def about(request):
    return render(request,'blog/about.html')

