'''
book: {
    title: ‘string’,
    author: ‘string’,
    year: 2011,
    description: ‘string’,
    genre: ‘string’,
    id: 0,
}

согласна шаблонам - добавил tags
'''

from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Book(models.Model):
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
    year = models.CharField(
        verbose_name='Год выпуска',
        max_length=200,
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Укажите, полное описание',
    )
    # возможно надо добавить choices
    genre = models.CharField(
        verbose_name="Жанры",
        max_length=200,
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name="Тег",
    )

    class Meta:
        ordering = ('title',)
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def list_tags(self):
        return self.tag.values_list('name', flat=True)

    def __str__(self):
        return self.title
