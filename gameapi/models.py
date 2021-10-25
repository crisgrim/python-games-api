from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    steam_user = models.CharField(blank=True, max_length=100)
    discord_user = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return self.email


class Game(models.Model):
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Party(models.Model):
    name = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.CharField(max_length=200)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    party_id = models.ForeignKey(Party, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
