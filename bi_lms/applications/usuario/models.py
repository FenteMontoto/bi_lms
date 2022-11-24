from django.db import models
from ckeditor.fields import RichTextField



class Skill(models.Model):
    skill = models.CharField("Logros", max_length=50)
    
    def __str__(self):
        return self.skill
    
    class Meta:
        verbose_name='Logro'
        verbose_name_plural='Logros'
        # Para ordenar por los campos seleccionados

        ordering=['skill']
    
    
class Usuario(models.Model):
    cod_gestor = models.CharField("Usuario", max_length=7, unique=True,default="")
    nombre = models.CharField("Nombre", max_length=20,default="")
    primer_ap = models.CharField("Primer apellido", max_length=20,default="")
    segundo_ap = models.CharField("Segundo apellido", max_length=20,default="")
    # nombre_completo = models.CharField("Nombre Completo", max_length=40,blank=True)
    email=models.EmailField("Email",blank=True, null=True)
    extension=models.IntegerField(default=0)
    job=models.CharField("Función",max_length=30,blank=True, null=True)
    delegacion=models.CharField("Delegación",max_length=30,blank=False, null=False,default="")
    grupo_titular=models.CharField("Grupo",max_length=30,blank=False, null=False,default="")
    servicio_titular=models.CharField("Servicio",max_length=30,blank=False, null=False,default="")
    # grupo_refuerzo=models.CharField(max_length=30,blank=True, null=True)
    # servicio_refuerzo_1=models.CharField(max_length=30,blank=True, null=True)
    # servicio_refuerzo_2=models.CharField(max_length=30,blank=True, null=True)
    # fecha_nacimiento=models.DateField()
    # fecha_incorporacion=models.DateField()
    # discapacidad=models.CharField(max_length=2)
    # reduccion_jornada=models.CharField(max_length=2)
    # horas_jornada=models.IntegerField()
    # imagen=models.ImageField(upload_to="gestion_usuarios", null=True, blank=True)
    skill = models.ManyToManyField(Skill)
    comentarios=RichTextField(blank=True, null=True,default="")
    
    def __str__(self):
        return self.cod_gestor
