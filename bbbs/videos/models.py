'''
video:  {
    id: 0,
    imageUrl: 'https://',
    title: ‘string,
    info: ‘str’ing,
    link: 'https://www.youtube',
    tag: {
      name: ‘string,
      id: 0,
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


class Video(models.Model):
    show_on_main_page = models.BooleanField(
        default=False,
        verbose_name='Показать на главной',
        help_text='Установить флаг, если проверено для публикации',
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    # надо посмотреть в figma, что имеется ввиду
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
        upload_to="videos/images",
    )
    file = models.FileField(
        upload_to="videos/uploaded",
        null=True,
    )
    link = models.URLField(
        max_length=200
    )

    class Meta:
        ordering = ('title',)
        verbose_name = "Видео"
        verbose_name_plural = "Видео"

    def __str__(self):
        return self.title
