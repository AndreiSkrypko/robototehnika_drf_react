# Импортируем функцию path для создания маршрутов
from django.urls import path

# Импортируем представление (view), которое будет обрабатывать запросы к /navbar/
from .views import navbar_data

# Список маршрутов, доступных через /api/ (так как они подключаются в корневом urls.py с префиксом 'api/')
urlpatterns = [

    # Маршрут /api/navbar/
    # Когда пользователь делает GET-запрос на этот адрес, вызывается функция navbar_data
    path('navbar/', navbar_data),
]
