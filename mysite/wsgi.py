import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

# Определяем путь к .env в корне проекта
BASE_DIR = Path(__file__).resolve().parent.parent
env_path = BASE_DIR / '.env'
load_dotenv(env_path)

# Определяем окружение
env = os.environ.get('DJANGO_ENV', 'development')
settings_module = f'mysite.settings.{env}'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()