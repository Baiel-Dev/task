# confing/__init__.py
from __future__ import absolute_import, unicode_literals

# Это нужно для того, чтобы Celery был настроен при старте проекта
from .celery import app as celery_app

__all__ = ('celery_app',)
