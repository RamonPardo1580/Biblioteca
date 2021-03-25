# Generated by Django 3.1.7 on 2021-03-16 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_auto_20210316_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='tags',
            field=models.ManyToManyField(to='biblioteca.Tag'),
        ),
    ]