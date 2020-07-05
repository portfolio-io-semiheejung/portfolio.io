from django.shortcuts import render, redirect,get_object_or_404
from portfolios.models import Skill
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from portfolios.forms import UsercontentForm 
from portfolios.models import Usercontent
from pprint import pprint
from .forms import PostForm, CommentForm
from .models import Post, Color, Comment

# Create your views here.
def index(request):
    return render(request,'mains/index.html')


def template(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    comments = Comment.objects.all()
    context = {        
        'posts': posts,
        'comment_form': comment_form,
        'comments' : comments,
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


@require_POST
def comment_create(request, pk):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save() 
    return redirect('mains:template')

   

