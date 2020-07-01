from django.shortcuts import render, redirect,get_object_or_404
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request,'mains/index.html')


def template(request):
    posts = Post.objects.all()
    print('-------------------------------------------',posts)
    context = {
        'posts': posts,
    }
    return render(request,'mains/template.html', context)


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
    return render(request, 'mains/form.html', context)

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
