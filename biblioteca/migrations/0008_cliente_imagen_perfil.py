# Generated by Django 3.1.7 on 2021-05-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_cliente_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagen_perfil',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
