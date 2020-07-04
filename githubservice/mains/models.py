from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, ResizeCanvas
# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='media')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    class Meta:
        ordering = ['-id']      


class Color(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    color1 = models.CharField(max_length=20)
    color2 = models.CharField(max_length=20)
    color3 = models.CharField(max_length=20)
    color4 = models.CharField(max_length=20)


class Comment(models.Model):
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #작성자는 user모델과 연결
    post = models.ForeignKey(Post, on_delete=models.CASCADE) #1개의 post에 여러개의 comment
