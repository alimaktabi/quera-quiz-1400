from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User as BaseUser


class User(BaseUser):
    first_name = None
    last_name = None

    name = models.CharField(max_length=500)

    username = None

    USERNAME_FIELD = 'email'


class Group(models.Model):

    name = models.CharField(max_length=300)

    description = models.TextField()

    members = JSONField()


