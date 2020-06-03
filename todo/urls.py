from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TodoList.as_view()),
    path('detail/<int:pk>', views.TodoDetail.as_view()),
]