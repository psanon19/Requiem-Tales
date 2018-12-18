from django.contrib import admin
from .models import PlayerCharacterModel, UserSetupModel, CharacterClassesModel

# Register your models here.
admin.site.register(PlayerCharacterModel)
admin.site.register(UserSetupModel)
admin.site.register(CharacterClassesModel)