from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    email_verify = models.BooleanField(default=False)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []