from django.db import models
from django.utils import timezone


class UserDAO(models.Model):
    user_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    password = models.TextField(max_length=100)
    c_time = models.DateTimeField(default=timezone.now)
    