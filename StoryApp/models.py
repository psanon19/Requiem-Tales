from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone


class CharacterClassesModel(models.Model):
    class_name = models.CharField(max_length=200,)
    hit_points = models.IntegerField(default=0)
    strength = models.IntegerField(default=0)
    magic = models.IntegerField(default=0)
    skill = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    faith = models.IntegerField(default=0)
    resistance = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    movement = models.IntegerField(default=0, null=True)
    description = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.class_name


class PlayerCharacterModel(models.Model):
    full_name = models.CharField(max_length=50, null=True)
    current_gold = models.IntegerField(default=0,)
    username = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,)
    strength = models.IntegerField(default=0)
    magic = models.IntegerField(default=0)
    skill = models.IntegerField(default=0)
    speed = models.IntegerField(default=0)
    faith = models.IntegerField(default=0)
    resistance = models.IntegerField(default=0)
    defence = models.IntegerField(default=0)
    constitution = models.IntegerField(default=0)
    movement = models.IntegerField(default=0)
    classFK = models.ForeignKey(CharacterClassesModel, on_delete=models.SET_NULL, null=True, blank=True)

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
