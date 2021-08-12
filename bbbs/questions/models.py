from django.db import models


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
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Question(models.Model):
    show_on_main_page = models.BooleanField(
        default=False,
        verbose_name='Показать на главной',
        help_text='Установить флаг, если проверено для публикации',
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Тег',
        help_text='Выберите один или несколько тегов',
        related_name='tags',
    )
    question = models.CharField(
        max_length=500,
        unique=True,
        verbose_name='Вопрос',
        help_text='Введите текст вопроса'
    )
    answer = models.TextField(
        verbose_name='Ответ на вопрос',
        help_text='Введите текст ответа',
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
