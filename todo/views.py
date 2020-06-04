from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from . import models
from django.urls import reverse_lazy

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = models.TodoModel

class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = models.TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = models.TodoModel
    
    # 生成時の入力対象データを指定(form.as_pに対応)
    fields = ('title', 'memo', 'priority', 'duedate')
    
    # データ作成成功時のURL指定
    # path名を指定してそれに紐づくURLに遷移する
    # class based viewで使う時はreverse_lazy()
    # function based viewではreverse()
    success_url = reverse_lazy('list')
