from django.db import models
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'description']),
        ]

    def __str__(self):
        return self.name
