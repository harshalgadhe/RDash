from . import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.task_page, name="task_page"),
    path('create_task', views.create_task, name="create_task"),
    path('save_task', views.save_task, name="save_task"),
    path('user_tasks', views.user_tasks, name='user_tasks')
]
