from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

from companies.models import Enterprise

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(unique=True)
    is_owner = models.BooleanField(default=True)

    # USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    

class Group(models.Model):
    name = models.CharField(max_length=150, blank=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)


class GroupPermission(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)