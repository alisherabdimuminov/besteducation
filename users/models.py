from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_payed = models.BooleanField(default=False)
    last_pay_date = models.DateField(null=True, blank=True)
    is_student = models.BooleanField(default=False)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.username
