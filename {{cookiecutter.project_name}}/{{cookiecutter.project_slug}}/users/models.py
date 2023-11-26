from django.db import models
from {{cookiecutter.project_slug}}.common.models import TimeStampedBaseModel

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _

from {{cookiecutter.project_slug}}.users.managers import BaseUserManager

class BaseUser(TimeStampedBaseModel, AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(verbose_name = _("email"),
                              unique=True)
    is_admin = models.BooleanField(default=False, verbose_name=_("is_admin"))

    objects = BaseUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, verbose_name=_("user"))
    bio = models.CharField(max_length=1000, null=True, blank=True, verbose_name=_("bio"))

    def __str__(self):
        return f"{self.user} profile"






