from django.urls import path
from . import views

app_name='mains'
urlpatterns = [
    path('',views.index, name='index'),
    path('template/', views.template, name='template'),
    path('create/', views.create, name='create'),
    path('<int:pk>/like/', views.like, name='like'),   
    path('guide/', views.guide, name='guide'),
    path('<int:pk>/comment/', views.comment_create, name='comment_create'),   
]    
