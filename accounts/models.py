from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    userimage = models.ImageField(blank=True, null=True, upload_to='userimages/')
    first_name = None
    last_name = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname',]
    objects = UserManager()

    def __str__(self):
        return self.email