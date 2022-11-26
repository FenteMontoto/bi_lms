from django.urls import path
from .import views

app_name='usuario_app'

urlpatterns = [
    path('home/',views.home.as_view(), name="Home"),
    path('login/',views.Login.as_view(), name='login'),
    path('logout/',views.Logout.as_view(), name='logout'),
    path('cambiarpass/',views.UpdatePass.as_view(), name='cambiarpass'),
]
