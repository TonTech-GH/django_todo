from django.contrib import admin
from . import models

# 管理画面の操作対象として登録
admin.site.register(models.TodoModel)