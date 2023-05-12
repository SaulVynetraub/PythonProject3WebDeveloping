#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#Ctrl + Z and Enter - выход из оболочки (Shell) Python
#Ctrl + C - остановка сервера разработки в терминальном окне
#python manage.py runserver - запуск (перезапуск) сервера разработки
#python manage.py shell - запуск интерактивной оболочки Python
#Fn + Ctrl + B - выход из сервера разработки
#python manage.py makemigrations learning_logs - изменение БД для хранения информации о новой модели
#python manage.py migrate - полная миграция, автоматическое изменение БД
#http://localhost:8000/topics/ - домашняя страница в браузере с разделами тем