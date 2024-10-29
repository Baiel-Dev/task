# task/cron.py
from django_cron import CronJobBase, Schedule
from .models import Task

class DailyTaskUpdate(CronJobBase):
    RUN_AT_TIMES = ['00:00']  # Запускается каждый день в полночь

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'task.daily_task_update'  # Уникальный код для задачи

    def do(self):
        # Здесь добавьте логику для обновления задач
        Task.objects.all().update(status=False)  # Сброс статуса всех задач
