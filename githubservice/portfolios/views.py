from django.shortcuts import render, redirect
import requests
from pprint import pprint
from datetime import datetime
from django.http import JsonResponse 
from requests.auth import HTTPBasicAuth
import json

#for a in d[0]['ssh_url']:
#    pprint(a)

def index(request):
    # username = request.GET['username']
    # url = 'https://api.github.com/users/%s' % username
    url = 'https://api.github.com/users/heejung-choi'
    response = requests.get(url, auth=HTTPBasicAuth('9cab848980beedfbdecb', 'a365a80d1e78e483f242d4a440b943509e4e4b85')).json()
    print(response)
    repo_url = 'https://api.github.com/users/heejung-choi/repos'       
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
        'repo_url': repo_url  
    },)

def about(request):
    color1 = '#e6dace'
    color2 = 'rgb(244,236,230)'
    color3 = 'blue'
    color4 = 'black'
    context = {
        'color1' : color1,
        'color2' : color2,
        'color3' : color3,
        'color4' : color4,
    }
    return render(request, 'portfolios/about.html', context)


def insert(request): 
    return render(request, 'portfolios/insert.html')
