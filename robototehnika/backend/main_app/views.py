from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def example_navbar_data(request):
    data = {
        "logo": "/static/main/img/logo.jpg",
        "links": [
            {"name": "О КЛУБЕ", "url": "/about"},
            {"name": "КОНТАКТЫ", "url": "/contacts"},
            {"name": "ФОРУМ", "url": "/forum_list"},
            {"name": "ВОЙТИ", "url": "/login"},
            {"name": "РЕГИСТРАЦИЯ", "url": "/register"},
        ]
    }
    return Response(data)

