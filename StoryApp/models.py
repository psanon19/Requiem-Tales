from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone



class PlayerCharacterModel(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    current_health = models.IntegerField(default=0,)
    current_gold = models.IntegerField(default=0,)
    current_strength = models.IntegerField(default=0,)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)

    #
    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

    def __str__(self):
        return self.full_name


class UserSetupModel(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=257)
    email = models.EmailField(max_length=200)
    nameFK = models.ForeignKey(PlayerCharacterModel, on_delete=models.SET_NULL, null=True, blank=True,)

    def __str__(self):
        return self.first_name