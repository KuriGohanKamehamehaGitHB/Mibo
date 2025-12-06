from django.shortcuts import render
from .models import Article

def main_page(request):
    # Получаем все статьи, сортируем от новых к старым
    articles = Article.objects.all().order_by('-release_date')
    return render(request, 'index.html', {'articles': articles})