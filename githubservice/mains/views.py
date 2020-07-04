from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post
from portfolios.models import Color
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    return render(request,'mains/index.html')


def template(request):
    posts = Post.objects.all()
    colors = Color.objects.all()
    #print('-------------------------------------------',posts)
    context = {
        'posts': posts,
        'colors':colors,
    }
    return render(request,'mains/template.html', context)

# 사용자가 입력하는건 아니고, 우리 db에 넣어서 template에 뿌릴 것
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('mains:index')
    else:
        form = PostForm()
    context ={
        'form' : form,
    }    
    return render(request, 'mains/t_form.html', context)


@login_required
def like(request, pk):
    user = request.user
    post = get_object_or_404(Post, pk=pk)

    if post in user.like_posts.all(): 
        user.like_posts.remove(post)
        liked = False
    else:
        user.like_posts.add(post)
        liked = True

    context = {
        'msg' : '좋아요 기능이 동작했습니다',
        'liked' : liked
    }
    return JsonResponse(context)


def guide(request):
    return render(request, 'mains/guide.html')


def detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment_form = CommentForm()
    comments = post.comment_set.filter(parent__isnull=True)
    context = {
        'post': post,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'mains/detail.html', context)


@require_POST
def comment_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm(request.POST)
    comments = post.comment_set.filter(parent__isnull=True)
    parent_pk = request.POST.get('parent_pk')
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        if parent_pk:
            comment.parent_id = pk
        comment.save()
    return redirect('mains:detail', pk)

   

