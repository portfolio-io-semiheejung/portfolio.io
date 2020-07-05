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
from mains.models import Color,Post
from .forms import UsercontentForm, ProjectForm, EducationForm, ExperienceForm, GithubForm
from .models import Usercontent, Skill, Project, Education, Experience, Github
from django.shortcuts import render, redirect, get_object_or_404

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
            return redirect('portfolios:project',usercontent.pk)
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

def project(request,pk):
    #content = Usercontent.objects.get(user_id=request.user.pk)    
    usercontent = Usercontent.objects.get(pk=pk)
    git_name = request.user.github_username   
    url = f'https://api.github.com/users/{git_name}'
    response = requests.get(url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).json()
    repo_url = f'https://api.github.com/users/{git_name}/repos'    
    repo_load = json.loads(requests.get(repo_url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).text)    
    repo_name = []
    for r in range(len(repo_load)):     
        repo_name.append(repo_load[r]['name'])       

    if request.method == 'POST':
        edu_form = EducationForm(request.POST)
        ex_form = ExperienceForm(request.POST)
        project_form = ProjectForm(request.POST, request.FILES)

        if edu_form.is_valid():
            edu = edu_form.save(commit=False)
            edu.usercontent = usercontent
            edu.save()     
            return redirect('portfolios:project',pk)

        if ex_form.is_valid():
            ex = ex_form.save(commit=False)
            ex.usercontent = usercontent
            ex.save()
            return redirect('portfolios:project',pk)

        if project_form.is_valid():
            project = project_form.save(commit=False)
            project.usercontent = usercontent
            project.save()
            return redirect('portfolios:project',pk)

    else:
        edu_form = EducationForm()
        ex_form = ExperienceForm()
        project_form = ProjectForm()

    context = {
        'edu_form' : edu_form,
        'ex_form' : ex_form,
        'project_form' : project_form,
        'usercontent' : usercontent,
        'repo_name': repo_name,
    }
    return render(request, 'portfolios/project.html', context)

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
    