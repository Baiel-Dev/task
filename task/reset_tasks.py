from django.core.management.base import BaseCommand
from task.models import Task

class Command(BaseCommand):
    help = 'Сбрасывает все задачи к состоянию "не выполнена"'

    def handle(self, *args, **kwargs):
        Task.objects.update(completed=False)
        self.stdout.write(self.style.SUCCESS('Все задачи сброшены к состоянию "не выполнена".'))
