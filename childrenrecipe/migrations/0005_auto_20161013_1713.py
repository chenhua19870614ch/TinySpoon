# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-13 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenrecipe', '0004_auto_20161013_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procedure',
            name='image',
            field=models.ImageField(blank=True, upload_to='exhibited_picture/%Y/%m/%d'),
        ),
    ]