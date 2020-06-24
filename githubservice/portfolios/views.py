from django.shortcuts import render, redirect
import requests
from pprint import pprint
from datetime import datetime
from django.http import JsonResponse 
import json

repo_url = 'https://api.github.com/users/heejung-choi/repos'
d = json.loads(requests.get(repo_url).text)    

# pprint(d[0])
pprint(d[0]['name'])
pprint(d[0]['html_url'])

#for a in d[0]['ssh_url']:
#    pprint(a)

def index(request):
    # username = request.GET['username']
    # url = 'https://api.github.com/users/%s' % username
    url = 'https://api.github.com/users/heejung-choi'
    response = requests.get(url).json()

    #repo_url = 'https://api.github.com/repos/heejung-choi/django'
    repo_url = 'https://api.github.com/users/heejung-choi/repos'
    repo_response = requests.get(repo_url).json()    
    
    #d = json.loads(requests.get(repo_url).text)
    print('------')
    #pprint(d)
    print('------')

   # print(repo_response[0].values('name'))
    return render(request,'portfolios/index.html',{
        'name': response['login'],
        'profile_img_url': response['avatar_url'],
        'email': response['email'],
        #'repo_name' : repo_response['name']
    })

    