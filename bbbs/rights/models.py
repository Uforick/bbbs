from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Тег')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Right(models.Model):
    show_on_main_page = models.BooleanField(
        default=False,
        verbose_name='Показать на главной странице'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название'
    )
    description = models.CharField(
        max_length=500,
        verbose_name='Описание'
    )
    text = models.TextField(
        verbose_name='Текст'
    )
    color = models.CharField(
        max_length=50,
        verbose_name='Цвет'
    )
    image = models.ImageField(
        blank=True,
        verbose_name='Картинка',
        upload_to='rights/'
    )
    tag = models.ManyToManyField(
        Tag, 
        verbose_name='Тег',
        related_name='rights',
    )
    
    class Meta:
        verbose_name = 'Права ребенка'
        verbose_name_plural = 'Права ребенка'
        ordering = ('title',)

    def __str__(self):
        return self.title

    def list_tags(self):
        return self.tag.values_list('name', flat=True)
        