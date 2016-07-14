# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-07 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atlas', '0004_auto_20160407_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadata',
            name='group',
            field=models.CharField(blank=True, help_text='Thema groep (optioneel)', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='metadata',
            name='title',
            field=models.CharField(blank=True, help_text='Titel thema', max_length=100, null=True),
        ),
    ]