# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-04 19:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0016_auto_20190404_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='category',
            field=models.CharField(choices=[('B', 'Bug'), ('F', 'Feature')], default='B', max_length=1),
        ),
    ]
