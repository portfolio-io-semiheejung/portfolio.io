from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.processors import ResizeToFill, ResizeToFit, ResizeCanvas
# Create your models here.

class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Github(models.Model):
    profile_img = models.ImageField()
    git_repourl = models.CharField(max_length=100)
    git_reponame = models.CharField(max_length=200)
    git_username = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Skillkind(models.Model):
    skill_kind_name = models.CharField(max_length=100)
    cust_allskill = models.ManyToManyField(Portfolio, related_name='allskill')
    cust_majorskill = models.ManyToManyField(Portfolio, related_name='majorskill')

class Skil(models.Model):
    skill_name = models.CharField(max_length=100)
    skill_img = models.CharField(max_length=200)
    skillkind = models.ForeignKey(Skillkind, on_delete=models.CASCADE)     
   
class Color(models.Model):
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20)
    color3 = models.CharField(max_length=20)
   

class Aboutme(models.Model):
    job = models.CharField(max_length=20)
    introduce = models.TextField(_(""))
class Education(models.Model):
    pass
