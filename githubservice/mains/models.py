from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill, ResizeToFit, ResizeCanvas

# Create your models here.

class Post(models.Model):
    content = models.CharField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    image = ProcessedImageField(upload_to='media', # 경로
                                processors=[ResizeToFill(500, 500)], #가로, 세로 길이
                                format='PNG',
                                options={'quality': 60}) # 원본에서 얼마만큼의 %의 화질?.. 용량문제와 이어짐
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    class Meta:
        ordering = ['-id']      

