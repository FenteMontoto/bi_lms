from django.urls import path
from .import views

app_name='usuario_app'

urlpatterns = [
    path('home/',views.home, name="Home"),
    path('login/',views.Login.as_view(), name='login'),
   
]
