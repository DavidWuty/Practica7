# Generated by Django 5.0.2 on 2024-03-08 06:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Juego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('idioma', models.CharField(choices=[('es', 'Español'), ('en', 'Ingles'), ('de', 'Aleman'), ('fr', 'Frances')], max_length=15)),
                ('edad', models.IntegerField()),
                ('no_adultos', models.IntegerField()),
                ('no_menores', models.IntegerField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]