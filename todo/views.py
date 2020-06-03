from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    model = models.TodoModel

