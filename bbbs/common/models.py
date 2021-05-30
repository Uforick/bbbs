from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from bbbs.common.validators import city_name_validator

User = get_user_model()


class City(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        help_text='Введите название города',
        max_length=30,
        validators=[city_name_validator],
        unique=True
    )
    is_primary = models.BooleanField(
        verbose_name='Главный',
        help_text='Укажите главный ли город',
        default=False
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = "Города"
        ordering = ('-is_primary', 'name')


class Profile(models.Model):
    class PermissionChoice(models.TextChoices):
        ADMIN = 'ADMIN', 'администратор'
        MODERATOR = 'MODERATOR', 'модератор'
        REGION_MODERATOR = 'REGION_MODERATOR', 'региональный модератор'
        MENTOR = 'MENTOR', 'наставник'

    user = models.OneToOneField(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=30,
        choices=PermissionChoice.choices,
        default=PermissionChoice.MENTOR,
    )
    city = models.ManyToManyField(
        City,
        help_text='Выберите один или несколько городов.<br>',
        related_name='profiles',
        verbose_name='Город'
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили'
        ordering = ('user__username',)

    @property
    def get_city(self):
        return self.city.all()

    @property
    def is_mentor(self):
        """Returns True if user has role mentor."""
        return self.role == self.PermissionChoice.MENTOR
            
    @property
    def is_moderator(self):
        """Returns True if user has role moderator."""
        return self.role == self.PermissionChoice.MODERATOR
        

    @property
    def is_region_moderator(self):
        """Returns True if user has role region moderator."""
        return self.role == self.PermissionChoice.REGION_MODERATOR
           

    @property
    def is_admin(self):
        """Returns True if user has role admin."""
        return self.role == self.PermissionChoice.ADMIN \
                or self.user.is_staff
        

@receiver(post_save, sender=Profile)
def change_user_profile_role(sender, **kwargs):
    instance = kwargs.get('instance')
    user = instance.user
    all_perms_event = Permission.objects.filter(codename__endswith='event')
    all_perms_сity = Permission.objects.filter(codename__endswith='city')
    all_perms_profile = Permission.objects.filter(codename__endswith='profile')
    all_perms_user = Permission.objects.filter(codename__endswith='user')

    # полные разрешения на Event, City, Profile, User
    if instance.role == Profile.PermissionChoice.ADMIN:
        user.user_permissions.clear()
        user.user_permissions.add(*all_perms_event)
        user.user_permissions.add(*all_perms_сity)
        user.user_permissions.add(*all_perms_profile)
        user.user_permissions.add(*all_perms_user)

    elif instance.role == Profile.PermissionChoice.MODERATOR:
        can_view_all_models = Permission.objects.filter(
            codename__startswith='view_'
        )
        user.user_permissions.clear()
        user.user_permissions.add(
            *can_view_all_models,
            *all_perms_сity
        )

    elif instance.role == Profile.PermissionChoice.REGION_MODERATOR:
        user.user_permissions.set(
            all_perms_event
        )

    elif instance.role == Profile.PermissionChoice.MENTOR \
        and not user.is_superuser:
        user.user_permissions.clear()
        user.is_staff = False
        user.save()


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    instance = kwargs.get('instance')
    if kwargs.get('created'):
        instance.is_stuff = False
        Profile.objects.create(user=instance)
