# Generated by Django 2.0.3 on 2018-03-17 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listado', '0003_auto_20180307_2205'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='foto',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='grupo',
            field=models.ManyToManyField(blank=True, to='listado.Grupo'),
        ),
    ]
