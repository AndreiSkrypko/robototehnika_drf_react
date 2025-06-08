from pathlib import Path
import os

# Корень проекта: robototehnika/
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Безопасность
SECRET_KEY = 'django-insecure-g#nou&7%8z!i$3a@-a(b!66o#a!m-j$ok(#&l3j0bzo4xth2=7'
DEBUG = True  # В продакшене поставить False
ALLOWED_HOSTS = ['*']  # Для продакшена указать домены (например, ['yourdomain.com'])

# Приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'main_app',
    'corsheaders',
]

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Всегда первым
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корень маршрутов
ROOT_URLCONF = 'backend.urls'

# Шаблоны — используем index.html из React build
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "backend" / "main_app" / "templates",  # туда копируем React build
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'backend.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'backend' / 'db.sqlite3',
    }
}

# Валидация паролей
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Локализация
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Настройка CORS (разрешаем React-доступ)
CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ Только для разработки
# Альтернатива безопаснее:
# CORS_ALLOWED_ORIGINS = ['http://localhost:3000']

# Статика (React и Django статические файлы)
STATIC_URL = '/static/'

# Где искать статические файлы во время разработки
STATICFILES_DIRS = [
    BASE_DIR / "backend" / "static",  # ручная статика
]

# Куда собрать всю статику для продакшена
STATIC_ROOT = BASE_DIR / "staticfiles"

# Настройка поля по умолчанию для моделей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
