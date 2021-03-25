# Generated by Django 3.1.7 on 2021-03-16 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_auto_20210315_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creada', models.DateTimeField(auto_now_add=True, null=True)),
                ('estatus', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En camino', 'En camino'), ('Entregado', 'Entregado')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('precio', models.FloatField(null=True)),
                ('categoria', models.CharField(choices=[('Libros', 'Libros'), ('Novelas', 'Novelas'), ('Historietas', 'Historietas'), ('Periodicos', 'Periodicos')], max_length=200, null=True)),
                ('descripccion', models.CharField(max_length=200, null=True)),
                ('fecha_creada', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]