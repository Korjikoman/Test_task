#!/usr/bin/env python
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def main():
    """Run administrative tasks."""
    # Определяем путь к .env в корне проекта
    BASE_DIR = Path(__file__).resolve().parent
    env_path = BASE_DIR / '.env'
    load_dotenv(env_path)
    
    # Определяем настройки
    django_env = os.environ.get('DJANGO_ENV', 'development')
    settings_module = f'mysite.settings.{django_env}'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()