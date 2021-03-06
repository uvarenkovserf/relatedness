# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-25 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AverageStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('avg_temperature', models.FloatField()),
                ('avg_wind_speed', models.FloatField()),
                ('avg_wind_vector', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='GeoPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinates', models.CharField(max_length=255)),
                ('height', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WeatherEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('temperature', models.FloatField()),
                ('wind_speed', models.FloatField()),
                ('wind_vector', models.FloatField()),
                ('geoposition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.GeoPosition')),
            ],
        ),
        migrations.AddField(
            model_name='averagestats',
            name='geoposition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.GeoPosition'),
        ),
    ]
