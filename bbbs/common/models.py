from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class City(models.Model):
    name = models.CharField(
        verbose_name= 'Город',
        help_text='Введите название города',
        max_length=30
    )
    is_primary = models.BooleanField(
        verbose_name= 'Основной',
        help_text='Укажите, если город является основным для вас',
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name',)


class Profile(models.Model):
    class PermissionChoice(models.TextChoices):
        ADMIN = 'ADMIN', 'администратор'
        MODERATOR = 'MODERATOR', 'модератор'
        REGION_MODERATOR = 'REGION_MODERATOR', 'региональный модератор'
        MENTOR = 'MENTOR', 'наставник' 

    user = models.OneToOneField(
        User,
        verbose_name= 'Пользователь', 
        on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=30,
        choices=PermissionChoice.choices,
        default=PermissionChoice.MENTOR,
    )
    city = models.OneToOneField(
        City, 
        verbose_name= 'Город',
        blank=True,
        null=True,
        on_delete=models.RESTRICT)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили'
        ordering = ('user',)
    
    
    @property
    def is_mentor(self):
        'Returns True if user has role mentor.'
        if self.role == self.PermissionChoice.MENTOR:
            return True
        return False

    @property
    def is_moderator(self):
        'Returns True if user has role moderator.'
        if self.role == self.PermissionChoice.MODERATOR:
            return True
        return False
    
    @property
    def is_region_moderator(self):
        'Returns True if user has role region moderator.'
        if self.role == self.PermissionChoice.REGION_MODERATOR:
            return True
        return False

    @property
    def is_admin(self):
        'Returns True if user has role admin.'
        if self.role == self.PermissionChoice.ADMIN or self.user.is_staff is True:
            return True
        return False


@receiver(post_save, sender=Profile)
def change_user_profile_role(sender, **kwargs):
    instance = kwargs.get('instance')
    user = instance.user
    if instance.role == 'REGION_MODERATOR':
        can_view_event_obj = Permission.objects.get(codename='view_event')
        can_view_eventparticipant_obj = Permission.objects.get(codename='view_eventparticipant')
        can_change_event_obj = Permission.objects.get(codename='change_event')
        can_change_eventparticipant_obj = Permission.objects.get(codename='change_eventparticipant')
        user.user_permissions.add(
            can_view_event_obj, can_view_eventparticipant_obj,
            can_change_event_obj,can_change_eventparticipant_obj,
        )


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    instance = kwargs.get('instance')
    if kwargs.get('created'):
        instance.is_stuff = False
        Profile.objects.create(user=instance)
