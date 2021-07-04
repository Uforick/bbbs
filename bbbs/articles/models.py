'''
article: {
    title: ‘string',
    author: ‘string,
    link: 'https://',
    text: ‘string,
    id: 0,
  }
'''

from django.db import models


class Article(models.Model):
    show_on_main_page = models.BooleanField(
        default=False,
        verbose_name='Показать на главной',
        help_text='Установить флаг, если проверено для публикации',
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    author = models.CharField(
        verbose_name="Автор",
        max_length=200,
    )
    link = models.URLField(
        verbose_name="Сайт",
        help_text="Введите адрес",
        null=True,
        blank=True,
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Укажите, полное описание',
    )

    class Meta:
        ordering = ('title',)
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
