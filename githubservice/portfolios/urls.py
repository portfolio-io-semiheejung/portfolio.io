from django.urls import path
from . import views

app_name = 'portfolios'
urlpatterns = [
    path('', views.index, name='index'),
    path('skill/', views.skill, name ='skill'),
    path('about/', views.about, name='about'),
    path('insert/', views.insert, name='insert'),
    path('<int:Usercontent_pk>/', views.detail, name='detail'),
    path('gitinfo/', views.gitinfo, name='gitinfo'),
]