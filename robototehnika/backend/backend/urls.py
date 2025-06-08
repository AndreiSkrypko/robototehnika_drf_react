# Импортируем админ-панель Django
from django.contrib import admin

# Импортируем функции для описания маршрутов
from django.urls import path, include, re_path

# Импортируем TemplateView — это встроенное представление, которое просто возвращает HTML-шаблон
from django.views.generic import TemplateView

# Основной список маршрутов (URL-ов), которые обрабатывает Django
urlpatterns = [

    # 1. Админ-панель Django доступна по адресу /admin/
    # Пример: http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),

    # 2. Все маршруты, начинающиеся с /api/, обрабатываются в файле main_app/urls.py
    # Это удобно для организации всех API-запросов в одном месте
    path('api/', include('main_app.urls')),

    # 3. Любой другой URL (не /admin/ и не /api/) отдаёт index.html
    # Это нужно, чтобы фронтенд-приложение (React) работало с маршрутизацией на клиенте
    # Например: /about, /contact — всё это будет возвращать index.html
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
]
