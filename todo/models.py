from django.db import models

# Create your models here.

PRIORITY = (('danger','high'), ('info','normal'), ('success','low'))

class TodoModel(models.Model):
    # カラム名 = モデルフィールド
    title = models.CharField(max_length=100)
    memo  = models.TextField()
    priority = models.CharField(max_length = 50, choices = PRIORITY)
    duedate = models.DateField()

    def __str__(self):
        '''オブジェクトを文字列として返す特殊メソッド'''
        return '{}: {}'.format(self.title, self.memo)