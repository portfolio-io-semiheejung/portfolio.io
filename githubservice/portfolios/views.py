from django.shortcuts import render, redirect
import requests
from pprint import pprint
from datetime import datetime
from django.http import JsonResponse 
from requests.auth import HTTPBasicAuth
import json
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from .forms import UsercontentForm
from .models import Usercontent
from accounts.models import User
from accounts.forms import CustomUserCreationForm
#for a in d[0]['ssh_url']:
#    pprint(a)

@login_required
def index(request):
    # username = request.GET['username']
    # url = 'https://api.github.com/users/%s' % username
    #userindex = User.objects.get(pk=2)
    #username = userindex.github_username
    #print(userindex)
    gitname = 'heejung-choi'
    url = 'https://api.github.com/users/'+gitname
    response = requests.get(url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).json()
    #print(response)
    repo_url = 'https://api.github.com/users/'+gitname+'/repos'       
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

    return render(request,'portfolios/index.html',{
        'name': response['login'],
        'profile_img_url': response['avatar_url'],
        'email': response['email'],
        'repo_name': repo_name,
        'repo_url': repo_url,
        
          
    },)

@login_required
def about(request):
    content = Usercontent.objects.get(pk=1)
    pprint(content)

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
            Usercontent = form.save()
            return redirect('portfolios:about', Usercontent.pk)
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
