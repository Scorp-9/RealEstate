# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:12
from __future__ import unicode_literals

import adverts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('image', models.ImageField(height_field=models.IntegerField(default=0), upload_to=adverts.models.upload_directory, verbose_name='Zdjęcie', width_field=models.IntegerField(default=0))),
            ],
        ),
        migrations.AlterField(
            model_name='advert',
            name='estate',
            field=models.CharField(choices=[('house', 'Dom'), ('plot', 'Działka'), ('flat', 'Mieszkanie'), ('investment', 'Inwestycja')], max_length=12, verbose_name='Typ nieruchomości'),
        ),
    ]