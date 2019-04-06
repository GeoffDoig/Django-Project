# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 17:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190329_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.
                                    CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
