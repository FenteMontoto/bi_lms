from django import forms
from django.contrib.auth import authenticate
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
  
    
    def clean(self):
        cleaned_data=super(LoginForm,self).clean()
        username=self.cleaned_data['username']
        password=self.cleaned_data['password']
        
        if not authenticate(username=username,password=password):
            raise forms.ValidationError('Los datos de usuario no son correctos')
        
        return self.cleaned_data
    

class UpdatePassForm(forms.Form):
    password1=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Contraseña Actual'}
        )
    )
    
    password2=forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Contraseña Nueva'}
        )
    )