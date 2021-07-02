'''
materials: {
    title: 'string',
    text: 'string',
    imageUrl: 'https:/',
    id: 0,
}
'''

from django.db import models


class Material(models.Model):
    show_on_main_page = models.BooleanField(
        default=False,
        verbose_name='Показать на главной',
        help_text='Установить флаг, если проверено для публикации',
    )
    title = models.CharField(
        verbose_name="Название",
        max_length=200,
    )
    text = models.TextField(
        verbose_name='Описание',
        help_text='Укажите, полное описание',
    )
    imageUrl = models.ImageField(
        verbose_name="Фото",
        help_text="Добавить фото",
        null=True,
        blank=True,
        upload_to="materials/images",
    )

    class Meta:
        ordering = ('title',)
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"

    def __str__(self):
        return self.title
