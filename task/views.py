from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import TaskForm
from .models import Task
from datetime import timedelta

def reset_tasks():
    # Сбрасывает все задачи к состоянию "не выполнена"
    Task.objects.update(completed=False, updated_at=timezone.now())


def list_task(request):
    tasks = Task.objects.all()
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        task = get_object_or_404(Task, id=task_id)  # Изменено
        task.completed = not task.completed  # Переключает состояние
        task.save()
        return redirect('list-task')  # Убедитесь, что это имя совпадает с urlpatterns

    return render(request, 'task/task_list.html', {'tasks': tasks})



def task_count(request):
    tasks = Task.objects.all()

    # Подсчет выполненных и невыполненных задач
    completed_tasks_count = tasks.filter(status=True).count()
    incomplete_tasks_count = tasks.filter(status=False).count()

    # Проверка на наличие задач и получение даты первой задачи
    if tasks.exists():
        first_task_date = tasks.earliest('created_at').created_at
        total_days = (timezone.now().date() - first_task_date.date()).days
    else:
        total_days = 0

    context = {
        'tasks': tasks,
        'completed_tasks_count': completed_tasks_count,
        'incomplete_tasks_count': incomplete_tasks_count,
        'total_days': total_days,
    }

    return render(request, 'task/count_task.html', context)


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = not task.status  # Переключение статуса задачи
    task.save()
    return redirect('list-task')
