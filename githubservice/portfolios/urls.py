from django.urls import path
from . import views

app_name = 'portfolios'
urlpatterns = [
    path('', views.index, name='index'),
    path('skill/', views.skill, name ='skill'),
    path('project/', views.project, name='project'), 
    path('about/', views.about, name='about'),    
    path('gitinfo/', views.gitinfo, name='gitinfo'),
]