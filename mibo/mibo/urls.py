from django.contrib import admin
from django.urls import path
from core.views import main_page  # Импортируем нашу функцию

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='home'), # Пустая строка означает главную страницу
]