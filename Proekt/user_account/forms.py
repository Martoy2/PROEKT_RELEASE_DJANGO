from .models import NewUser
from django.forms import TextInput, ModelForm, FileInput


class AuthForm(ModelForm):
    class Meta:
        model = NewUser
        fields = ["email", "password"]
        widgets = {
            "email": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            "password": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль',
                'type': 'password',
                'autocomplete': 'current-password',
            }),
        }


class ProfileImage(ModelForm):
    class Meta:
        model = NewUser
        fields = ['user_image']
        widgets = {
            'user_image': FileInput(attrs={
                'class': ' form-control',
            })
        }