from django.shortcuts import render, redirect
import requests
from pprint import pprint
from datetime import datetime
from django.http import JsonResponse 
import json

#for a in d[0]['ssh_url']:
#    pprint(a)

def index(request):
    # username = request.GET['username']
    # url = 'https://api.github.com/users/%s' % username
    url = 'https://api.github.com/users/heejung-choi'
    response = requests.get(url).json()

    #repo_url = 'https://api.github.com/repos/heejung-choi/django'
    
    repo_url = 'https://api.github.com/users/heejung-choi/repos'
    repo_load = json.loads(requests.get(repo_url).text)    

    #pprint(d[0])
    #pprint(d[0]['name'])
    #pprint(d[0]['html_url'])
    #pprint(len(d))

    repo_name = []
    repo_url = []
    for r in range(len(repo_load)):
        pprint(repo_load[r]['name'])
        pprint(repo_load[r]['html_url'])
        repo_name.append(repo_load[r]['name'])
        repo_url.append(repo_load[r]['html_url'])        
    
    pprint("---------------------")
    pprint(repo_name)  

   # print(repo_response[0].values('name'))
    return render(request,'portfolios/index.html',{
        'name': response['login'],
        'profile_img_url': response['avatar_url'],
        'email': response['email'],
        'repo_name': repo_name,
        'repo_url': repo_url,  
    },)

    