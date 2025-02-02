# Generated by Django 5.1.2 on 2024-10-29 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, verbose_name='Key link')),
                ('name', models.CharField(max_length=120, verbose_name='Red social')),
                ('url', models.URLField(blank=True, max_length=350, null=True, verbose_name='Enlace')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='Icono')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Red social ',
                'verbose_name_plural': 'Redes sociales',
                'ordering': ['name'],
            },
        ),
    ]
