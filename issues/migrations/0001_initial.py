# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('screenshot', models.ImageField(blank=True,
                                                 upload_to='images')),
                ('reported_date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('O', 'Open'),
                                                     ('P', 'In Progress'),
                                                     ('F', 'Fixed')],
                                            default='O',
                                            max_length=1)),
                ('category', models.CharField(choices=[('C', 'Category'),
                                                       ('B', 'Bug'),
                                                       ('F', 'Feature')],
                                              default='C',
                                              max_length=1)),
                ('votes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
            ],
        ),
    ]
