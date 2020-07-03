from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.processors import ResizeToFill, ResizeToFit, ResizeCanvas
# Create your models here.

class Color(models.Model):
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20)
    color3 = models.CharField(max_length=20)
    color4 = models.CharField(max_length=20)


class Portfolio(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

class Github(models.Model):
    profile_img = models.CharField(max_length=200)
    git_repourl = models.CharField(max_length=200)
    git_reponame = models.CharField(max_length=200)
    git_username = models.CharField(max_length=200)
    git_email = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Skillkind(models.Model):
    skill_kind_name = models.CharField(max_length=20)
    cust_allskill = models.ManyToManyField(Portfolio, related_name='allskill')
    cust_majorskill = models.ManyToManyField(Portfolio, related_name='majorskill')

class Skil(models.Model):
    skill_name = models.CharField(max_length=20)
    skill_img = models.CharField(max_length=200)
    skillkind = models.ForeignKey(Skillkind, on_delete=models.CASCADE)     
   

class Aboutme(models.Model):
    job = models.CharField(max_length=15)
    introduce = models.CharField(max_length=200)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

class Develop(models.Model):
    develop_content = models.CharField(max_length=15)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

class Education(models.Model):
    edu_name = models.CharField(max_length=20)
    edu_content = models.TextField()
    edu_data_start = models.DateField()
    edu_data_finish = models.DateField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)

class Experience(models.Model):
    ex_name = models.CharField(max_length=20)
    ex_content = models.TextField()
    ex_data_start = models.DateField()
    ex_data_finish = models.DateField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-ex_data_start']

class Project(models.Model):
    project_name = models.CharField(max_length=20)
    project_start = models.DateField()
    project_finsh = models.DateField()
    project_role = models.CharField(max_length=20)
    project_skill = models.CharField(max_length=200)
    project_content = models.TextField()
    project_img = models.ImageField()
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-project_start']     