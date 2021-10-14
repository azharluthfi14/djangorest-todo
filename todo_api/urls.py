from django.urls import path, include
from rest_framework import views
from todo_api.views import DetailTodo, ListTodo
from todo_api.views import (TodoList, TodoDetail)
from . import views

urlpatterns = [

    # Generic Class Based View
    path('todo/', TodoList.as_view(), name='todo_list'),
    path('todo/<int:pk>', TodoDetail.as_view(), name='todo_detail'),

    # Function Based View
    # path('todo/', views.todo_list, name='todo-list'),
    # path('todo/<int:pk>', views.todo_detail, name='todo-detail'),

    # Class Based View
    # path('todo/', ListTodo.as_view(), name='todo-list'),
    # path('todo/<int:pk>', DetailTodo.as_view(), name='todo-detail'),

]
