from django.shortcuts import render, HttpResponse
from django.views.generic.edit import (FormView)
from django.urls import reverse_lazy
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .models import Usuario
# Create your views here.

def home(request):
    

    return render(request,'usuario/home.html',({"title":"Inicio"}))


class Login(FormView):
    template_name='usuario/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('usuario_app:Home')
    
    def form_valid(self,form):
        user=authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(self.request,user)
        return super(Login,self).form_valid(form)
    
       