from django import forms
from .models import PlayerCharacterModel, UserSetupModel


class PlayerCharacterForm(forms.ModelForm):
    class Meta:
        model = PlayerCharacterModel
        fields = ['full_name','classFK']


class UserForm(forms.ModelForm):
    class Meta:
        model = UserSetupModel
        fields = ['first_name','email', 'password',]
        widgets = {
            'password': forms.PasswordInput(),
        }

