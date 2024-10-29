from django.urls import path
from . import views
urlpatterns = [
    path('tasks/', views.list_task, name='list-task'),
    path('tasks/<int:pk>/toggle/', views.toggle_task_status, name='toggle-task-status'),
    path('count/', views.task_count, name='count-task')
]

