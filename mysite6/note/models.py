from django.db import models
from user.models import User
# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=50,
                           verbose_name='標題')
    content=models.TextField(verbose_name='內容')
    create_time=models.DateTimeField(auto_now_add=True,
                                     verbose_name='創建時間')
    mod_time=models.DateTimeField(auto_now=True,
                                  verbose_name='修改時間')
    user=models.ForeignKey(User)