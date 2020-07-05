from django.shortcuts import render, redirect
import requests
from pprint import pprint
from datetime import datetime
from django.http import JsonResponse 
from requests.auth import HTTPBasicAuth
import json
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from accounts.forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from mains.models import Color, Post
from .forms import UsercontentForm, GithubForm
from .models import Usercontent, Skill, Github
from accounts.models import User

#for a in d[0]['ssh_url']:
#    pprint(a)
User = get_user_model()

@login_required
def index(request):
    git_name = request.user.github_username
    pprint("여기========================================")
    pprint(git_name)
    url = f'https://api.github.com/users/{git_name}'
    #url = 'https://api.github.com/users/heejung-choi'
    response = requests.get(url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).json()
    repo_url = f'https://api.github.com/users/{git_name}/repos'
    #repo_url = 'https://api.github.com/users/heejung-choi/repos' 
    repo_load = json.loads(requests.get(repo_url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).text)    

    repo_name = []
    repo_url = []
    for r in range(len(repo_load)):
        #pprint(repo_load[r]['name'])
        #pprint(repo_load[r]['html_url'])
        #repo_name.append(repo_load[r]['name']+": "+repo_load[r]['html_url'])
        repo_name.append(repo_load[r]['name'])
        repo_url.append(repo_load[r]['html_url'])   
    pprint("---------------------")
    #pprint(repo_name)
  
    context = {
        'name': response['login'],
        'profile_img_url': response['avatar_url'],
        'email': response['email'],
        'repo_name': repo_name,
        'repo_url': repo_url,
    }

    return render(request,'portfolios/index.html', context)


@login_required
def skill(request):
    posts = Post.objects.all()
    colors = Color.objects.all()
    skills = Skill.objects.all()
    if request.method == 'POST':
        form = UsercontentForm(request.POST)        
        if form.is_valid():            
            usercontent = form.save(commit=False)
            usercontent.user = request.user
            usercontent.save()
            pprint(request.POST.getlist('all_skills'))
            for skill in request.POST.getlist('all_skills'):
                usercontent.all_skills.add(skill)
            usercontent.save()
            return redirect('portfolios:about')
    # POST가 아닌 다른 methods 일 때
    else: 
        form = UsercontentForm()

    pprint(form.fields)  
    context = {
        'posts' : posts,
        'colors': colors,
        'skills': skills,
        'form': form,     
    }
    return render(request,'portfolios/skill.html', context)  

@login_required
def about(request):
    content = Usercontent.objects.get(user_id=request.user.pk)
    #pprint(content)
    color1 = '#e6dace'
    color2 = 'rgb(244,236,230)'
    color3 = 'blue'
    color4 = 'black'
    context = {
        'color1' : color1,
        'color2' : color2,
        'color3' : color3,
        'color4' : color4,
        'content': content
        
    }
    return render(request, 'portfolios/about.html', context)
    
@login_required
def insert(request):
    if request.method == 'POST':
        form = UsercontentForm(request.POST)
        if form.is_valid():
            Usercontent = form.save(commit=False)
            Usercontent.user = request.user
            Usercontent.save()
            return redirect('portfolios:about')
    # POST가 아닌 다른 methods 일 때
    else: 
        form = UsercontentForm()
    context = {        
        'form': form,
    }   
    return render(request, 'portfolios/insert.html', context)


@login_required
def detail(request, Usercontent_pk):
    Usercontent = Usercontent.objects.get(pk=Usercontent.pk)
    form = UsercontentForm()

    context = {
        'Usercontent': Usercontent,
        'form' : form,
    }
    return render(request, 'movies/detail.html', context)


def gitinfo(request): 
    git_name = request.user.github_username
    user = User.objects.get(pk=request.user.pk)
    git = Github.objects.get(pk=Github_pk) 
    print('--------------------------',user)
    print('--------------------------',git)
    git_name = request.user.github_username
    pprint(git_name)
    url = f'https://api.github.com/users/{git_name}'
    response = requests.get(url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).json()
    repo_url = f'https://api.github.com/users/{git_name}/repos'
    repo_load = json.loads(requests.get(repo_url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).text)    

    repo_name = []
    repo_url = []
    for r in range(len(repo_load)):
        repo_name.append(repo_load[r]['name'])
        repo_url.append(repo_load[r]['html_url'])   
    pprint("---------------------")

    if request.method == 'POST':
        form = GithubForm(request.POST, pk=Github_pk)
        if form.is_valid():
            github = form.save(commit=False)
            github.user = request.user
            git_email = 123
            git_reponame =123
            git_username =123
            github.save()
            return redirect('portfolios:skill')
    else:  
        form = GithubForm()      
   
    context = {
        'form' : form,
        # 'name': response['login'],
        # 'profile_img_url': response['avatar_url'],
        # 'email': response['email'],
        # 'repo_name': repo_name,
        # 'repo_url': repo_url,
    }
    return render(request, 'portfolios/index.html', context)

# def polls(request, poll_id):
#     poll = Poll.objects.get(pk = poll_id)#Poll객체를 구분하는 녀석은 poll_id이므로 PK지정
#     selection = request.POST['choice']
 
#     try:
#         #choice모델을 불러와서 1을 증가시킨다 
#         github = Github.objects.get(poll_id = poll.id, candidate_id = selection)
#         choice.votes += 1
#         choice.save()
#     except:
#         #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성합니다
#         choice = Choice(poll_id = poll.id, candidate_id = selection, votes = 1)
#         choice.save()


