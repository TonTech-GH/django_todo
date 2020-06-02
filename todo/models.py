from django.db import models

# Create your models here.
class TodoModel(models.Model):
    # カラム名 = モデルフィールド
    # title = models.CharField(max_length=100)
    title = models.CharField()
    memo  = models.TextField()