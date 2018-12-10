from django.contrib import admin
from .models import PlayerCharacterModel, UserSetupModel

# Register your models here.
admin.site.register(PlayerCharacterModel)
admin.site.register(UserSetupModel)