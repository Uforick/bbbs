from django.db import models

from pytils.translit import slugify


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        help_text='Введите имя тега',
        max_length=50, 
        unique=True
    )
    slug = models.SlugField(
        verbose_name='Ссылка',
        help_text='Заполняется автоматически',
        auto_created=True,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('-name',)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Question(models.Model):
    show_on_main = models.BooleanField(
        default = False,
        verbose_name='Показать на главной',
        help_text='Установить флаг, если проверено для публикации',
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        help_text='Выберите один или несколько тегов',
        related_name='tags',
        blank=True
    )
    question = models.CharField(
        max_length=500, 

        unique=True,
        verbose_name='Вопрос'
    )
    answer = models.TextField(
        verbose_name='Ответ на вопрос',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def list_tags(self):
        return self.tag.values_list('name', flat=True)

    def __str__(self):
        return self.question
