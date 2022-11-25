from django import forms
from .models import Usuario


class LoginForm(forms.Form):
    username=forms.CharField(
        label='Usuario',
        required=True,
        widget=forms.TextInput(
            attrs={'placeholder':'Usuario'}
        )
    )
    password=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Contraseña'}
        )
    )