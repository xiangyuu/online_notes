from django.db import models

# Create your models here.

class User(models.Model):
    username=models.CharField(max_length=30,
                              verbose_name='用戶名',
                              unique=True)
    password=models.CharField(max_length=30,
                              verbose_name='密碼')
    def __str__(self):
        return '用戶名：'+self.username

