from celery import shared_task
from task.models import Task

@shared_task
def reset_task_status():
    Task.objects.filter(status=True).update(status=False)
    print("Задача обновления статуса выполнена!")
    return "Статус задач сброшен"

@shared_task
def add(x, y):
    result = x + y
    print(f"Task completed: {x} + {y} = {result}")
    return result

