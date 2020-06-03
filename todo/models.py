from django.db import models

# Create your models here.
class TodoModel(models.Model):
    # カラム名 = モデルフィールド
    title = models.CharField(max_length=100)
    memo  = models.TextField()

    def __str__(self):
        '''オブジェクトを文字列として返す特殊メソッド'''
        return '{}: {}'.format(self.title, self.memo)