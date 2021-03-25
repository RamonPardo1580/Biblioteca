# Generated by Django 3.1.7 on 2021-03-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('telefono', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('fecha_creada', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
