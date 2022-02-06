from django.db import models
from django.contrib.auth.models import User
from .forms import UserCreationForm


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'
