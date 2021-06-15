from django.db import models


class RightTag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Тег')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='Слаг')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Right(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description = models.CharField(max_length=500, verbose_name='Описание')
    text = models.TextField(verbose_name='Текст')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    image = models.ImageField(blank=True, verbose_name='Картинка',
                              upload_to='rights/')
    tag = models.ManyToManyField(RightTag, verbose_name='Теги',
                                 related_name='rights')

    show_on_main_page = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Права ребенка'
        verbose_name_plural = 'Права ребенка'
        ordering = ('title',)

    def __str__(self):
        return self.title
