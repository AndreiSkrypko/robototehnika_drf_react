from django.urls import path
from .views import example_navbar_data

urlpatterns = [
    path('navbar/', example_navbar_data),  # /api/navbar/
]
