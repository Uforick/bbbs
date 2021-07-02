'''
book: {
    title: ‘string’,
    author: ‘string’,
    year: 2011,
    description: ‘string’,
    genre: ‘string’,
    id: 0,
}
'''

from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

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
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='books',
        help_text='Выберите автора'
    )
    year = models.DateField(
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Укажите, полное описание',
    )
    # возможно надо добавить choices - не нашел инфу по этому
    genre = models.CharField(
        verbose_name="Жанры",
        max_length=200,
    )

    class Meta:
        ordering = ('title',)
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.title
