from django.db import models

class Categories(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Posts(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    category = models.ForeignKey('Categories', null=True, on_delete=models.SET_NULL)
    content = models.TextField(verbose_name="Текст статьи")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
