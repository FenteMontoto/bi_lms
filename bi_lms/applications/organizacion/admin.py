from django.contrib import admin
from .models import Organizacion
# Register your models here.


class Organizacion_Admin(admin.ModelAdmin):
    list_display=(
        'delegacion',
        'grupo',
        'servicio',
    )
    search_fields=(
        'delegacion',
        'grupo',
        'servicio',
    )
    list_filter=(
        'delegacion',
        'grupo',
        'servicio',
    )
    
admin.site.register(Organizacion,Organizacion_Admin)