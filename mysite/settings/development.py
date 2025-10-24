from .base import *

DEBUG = True

# Для разработки разрешаем все хосты
ALLOWED_HOSTS = ['*']

# SQLite для разработки (опционально)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Отключаем WhiteNoise в разработке
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Логирование в консоль
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}