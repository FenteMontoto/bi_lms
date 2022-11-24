from django.db import models

# Create your models here.

class Organizacion(models.Model):
 
    delegacion = models.CharField("Delegación",max_length=20)
    grupo = models.CharField("Grupo",max_length=25)
    servicio = models.CharField("Servicio",max_length=20)
    
    class Meta:
        verbose_name='Organizacion'
        verbose_name_plural='Organizaciones'
        # Para ordenar por los campos seleccionados

        ordering=['delegacion','grupo']
        
        # si quisieramos descendente colocamos el signo "-" en el campo correspondiente
        
        # ordering=['-delegacion','grupo']
        
        # Para no permitir que se registren campos coincidentes
        
        unique_together=('delegacion','grupo','servicio')
    
    def __str__(self):
        return self.servicio

  