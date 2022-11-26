from django.shortcuts import render, HttpResponse
from django.views.generic.edit import (FormView)
from django.urls import reverse_lazy, reverse
from .forms import LoginForm, UpdatePassForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import (View,TemplateView)
from .models import Usuario
# Create your views here.



class home(LoginRequiredMixin, TemplateView):
    template_name = "usuario/home.html"
    # a donde redirigir en caso de que no este logado
    login_url=reverse_lazy('usuario_app:login')



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
    

    
class Logout(View):
    
    def get(self,request,*args,**kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse('usuario_app:login')
        )
        
    
class UpdatePass(LoginRequiredMixin, FormView):
    template_name='usuario/cambiar_pass.html'
    form_class=UpdatePassForm
    success_url=reverse_lazy('usuario_app:login')
    
    # a donde redirigir en caso de que no este logado
    login_url=reverse_lazy('usuario_app:login')
    
    def form_valid(self,form):
        usuario=self.request.user
        user=authenticate(
            username=usuario.username,
            password=form.cleaned_data['password1'],
        )
        if user:
            new_pass=form.cleaned_data['password2']
            usuario.set_password(new_pass)
            usuario.save()
            
        # Hacemos logout para que vuelva a logarse con la nueva pass   
        logout(self.request)
        return super(UpdatePass,self).form_valid(form)
    
        