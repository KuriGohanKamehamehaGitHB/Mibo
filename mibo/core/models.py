from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст статьи")
    # auto_now_add=True автоматически ставит текущую дату при создании
    release_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата выхода")
    image_url = models.URLField(verbose_name="Ссылка на картинку")
    
    # (Опционально) Связь с категорией, если захотите расширить функционал
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title