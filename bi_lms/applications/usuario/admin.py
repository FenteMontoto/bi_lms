from django.contrib import admin
from .models import Usuario, Skill
# Register your models here.

admin.site.register(Skill)


class Usuario_Admin(admin.ModelAdmin):
    list_display=(
        'cod_gestor',
        'delegacion',
        'grupo_titular',
    )

    search_fields=(
        'cod_gestor',
        'delegacion',
        'grupo_titular',
    )
    list_filter=(
        'delegacion',
        'grupo_titular',
        'skill',
    )
    filter_horizontal=('skill',)
    
   
    
class Logros_Admin(admin.ModelAdmin):
    list_display=(
        'skill',
    )
    
    

    
admin.site.register(Usuario,Usuario_Admin)