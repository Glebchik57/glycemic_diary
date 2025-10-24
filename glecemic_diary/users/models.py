from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class BaseUser(AbstractBaseUser):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    def __str__(self):
        return f'{self.surname} {self.name}'

    def get_short_name(self):
        return f'{self.surname} {self.name[0]}'

    class Meta:
        abstract = True


class Patient(BaseUser):
    insulin = models.CharField(max_length=100)
    guests = models.ManyToManyField(
        'Guest',
        related_name='patients',
        blank=True,
        verbose_name='Гости'
    )


class Guest(BaseUser):
    pass
