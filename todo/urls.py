from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TodoList.as_view(), name='list'),
    # int型のprimary_keyを使う指定
    path('detail/<int:pk>', views.TodoDetail.as_view(), name='detail'),
    path('create/', views.TodoCreate.as_view(), name='create'),
]