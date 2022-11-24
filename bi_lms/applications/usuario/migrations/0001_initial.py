# Generated by Django 4.1.3 on 2022-11-24 17:32

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Skill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("skill", models.CharField(max_length=50, verbose_name="Logros")),
            ],
            options={
                "verbose_name": "Logro",
                "verbose_name_plural": "Logros",
                "ordering": ["skill"],
            },
        ),
        migrations.CreateModel(
            name="Usuario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "cod_gestor",
                    models.CharField(
                        default="", max_length=7, unique=True, verbose_name="Usuario"
                    ),
                ),
                (
                    "nombre",
                    models.CharField(default="", max_length=20, verbose_name="Nombre"),
                ),
                (
                    "primer_ap",
                    models.CharField(
                        default="", max_length=20, verbose_name="Primer apellido"
                    ),
                ),
                (
                    "segundo_ap",
                    models.CharField(
                        default="", max_length=20, verbose_name="Segundo apellido"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, null=True, verbose_name="Email"
                    ),
                ),
                ("extension", models.IntegerField(default=0)),
                (
                    "job",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Función"
                    ),
                ),
                (
                    "delegacion",
                    models.CharField(
                        default="", max_length=30, verbose_name="Delegación"
                    ),
                ),
                (
                    "grupo_titular",
                    models.CharField(default="", max_length=30, verbose_name="Grupo"),
                ),
                (
                    "servicio_titular",
                    models.CharField(
                        default="", max_length=30, verbose_name="Servicio"
                    ),
                ),
                (
                    "comentarios",
                    ckeditor.fields.RichTextField(blank=True, default="", null=True),
                ),
                ("skill", models.ManyToManyField(to="usuario.skill")),
            ],
        ),
    ]
