from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, ResizeCanvas

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=200)
    image = ProcessedImageField(upload_to='%Y/%m/%d', # 경로
                                processors=[ResizeToFill(500, 400)], 
                                format='JPEG',
                                options={'quality': 60}) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    

    class Meta:
        ordering = ['id']      

