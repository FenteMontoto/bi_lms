from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    

    return render(request,'usuario/home.html',({"title":"Inicio"}))