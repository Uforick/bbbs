'''
movie: {
    id: 0,
    imageUrl: 'https://',
    title: ‘string’,
    info: string,
    link: 'https://www.youtube',
    tags: [
      {
        id: 0,
        name: ‘string’,
        slug: ‘string’,
      }
    ],
}
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


class Movie(models.Model):
    show_on_main_page = models.BooleanField(
        default=False,
        verbose_name='Показать на главной',
        help_text='Установить флаг, если проверено для публикации',
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    info = models.CharField(
        verbose_name="Инфо",
        max_length=200,
    )
    link = models.URLField(
        verbose_name="Сайт",
        help_text="Введите адрес сайта",
        null=True,
        blank=True,
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name="Тег",
    )
    imageUrl = models.ImageField(
        verbose_name="Фото",
        help_text="Добавить фото",
        null=True,
        blank=True,
        upload_to="movies/images",
    )

    class Meta:
        ordering = ('title',)
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

    def list_tags(self):
        return self.tag.values_list('name', flat=True)
    
    def __str__(self):
        return self.title
