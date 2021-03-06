from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, ResizeCanvas
from mains.models import Color
# Create your models here.

class Github(models.Model):
    git_reponame = models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.git_reponame

class Skill(models.Model):
    skill_kind = models.CharField(max_length=20)  
    skill_name = models.CharField(max_length=100)
    skill_img = models.CharField(max_length=200)


class Usercontent(models.Model):
    job = models.CharField(max_length=15)
    introduce = models.CharField(max_length=200)
    develop_content1 = models.CharField(max_length=20)
    develop_content2 = models.CharField(max_length=20)
    develop_content3 = models.CharField(max_length=20)
    develop_content4 = models.CharField(max_length=20)
    develop_content5 = models.CharField(max_length=20)
    develop_content6 = models.CharField(max_length=20)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True)
    all_skills = models.ManyToManyField(Skill, related_name='all_contents', null=True)
    def __str__(self):
        return self.introduce

class Project(models.Model):
    project_name = models.CharField(max_length=20)
    project_start = models.DateField()
    project_finsh = models.DateField()
    project_role = models.CharField(max_length=20)
    project_skill = models.CharField(max_length=200)
    project_content = models.TextField()
    project_img = models.ImageField(upload_to='media',blank=True)
    Usercontent = models.ForeignKey(Usercontent, on_delete=models.CASCADE, null=True)    
    github = models.OneToOneField(Github, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['-project_start']    
 
class Education(models.Model):
    edu_name = models.CharField(max_length=20)
    edu_content = models.TextField()
    edu_data_start = models.DateField()
    edu_data_finish = models.DateField()
    usercontent = models.ForeignKey(Usercontent, on_delete=models.CASCADE, null=True)
    class Meta:
        ordering = ['-edu_data_start']

class Experience(models.Model):
    ex_name = models.CharField(max_length=20)
    ex_content = models.TextField()
    ex_data_start = models.DateField()
    ex_data_finish = models.DateField()
    usercontent = models.ForeignKey(Usercontent, on_delete=models.CASCADE, null=True) 
    class Meta:
        ordering = ['-ex_data_start']
