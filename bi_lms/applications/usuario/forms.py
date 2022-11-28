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
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Contraseña Actual'}
        )
    )
    
    password2=forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Contraseña Nueva'}
        )
    )
    password3=forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Confirmar Contraseña'}
        )
    )
    def clean(self):
        cleaned_data=super(UpdatePassForm,self).clean()
        username1=self.cleaned_data['password2']
        username2=self.cleaned_data['password3']
        
        if not (username1==username2):
            raise forms.ValidationError('Las contraseñas proporcionadas no coinciden, por favor, vuelve a intentarlo')
        
        return self.cleaned_data