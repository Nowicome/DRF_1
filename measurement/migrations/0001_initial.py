# Generated by Django 5.0.2 on 2024-02-18 11:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Температура')),
                ('measurement_time', models.DateTimeField(auto_now_add=True, verbose_name='Время измерения')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='measurement.sensor')),
            ],
        ),
    ]