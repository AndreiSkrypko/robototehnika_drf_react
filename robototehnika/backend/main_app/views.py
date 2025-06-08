# Импортируем JsonResponse — это специальный тип ответа, который возвращает данные в формате JSON
from django.http import JsonResponse

# Импортируем настройки проекта (на всякий случай, если потребуется BASE_DIR и другие параметры)
from django.conf import settings

# Представление (view), которое будет обрабатывать запросы к /api/navbar/
def navbar_data(request):

    # Возвращаем JSON-ответ, содержащий логотип и ссылки меню
    # request.build_absolute_uri(...) — генерирует абсолютный путь к логотипу (например, http://127.0.0.1:8000/static/main/img/logo.jpg)
    return JsonResponse({
        "logo": request.build_absolute_uri("/static/main/img/logo.jpg"),  # Ссылка на логотип (путь к изображению)

        "links": [  # Список пунктов навигации — то, что будет отображаться в Navbar на фронтенде
            {"name": "Главная", "url": "/"},         # Ссылка на главную страницу
            {"name": "О нас", "url": "/about"},      # Ссылка на страницу "О нас"
            {"name": "Контакты", "url": "/contact"}, # Ссылка на страницу "Контакты"
        ]
    })

