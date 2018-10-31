from django.db import models
from django.utils import timezone

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    published_time = models.DateTimeField(blank=True, null=True)
    c_time = models.DateTimeField(default=timezone.now)
    