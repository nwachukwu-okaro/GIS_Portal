from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    """Portal account authenticated by unique email address and password."""

    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        permissions = [
            ('upload_data', 'Can upload data to MinIO and PostGIS'),
        ]

    def __str__(self):
        return self.get_full_name() or self.email


class Profile(models.Model):
    """Optional Systra business information kept separate from authentication."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    organisation = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=200, blank=True)
    job_title = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'Profile for {self.user.email}'

