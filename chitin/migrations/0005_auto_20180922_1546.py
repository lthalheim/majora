# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-22 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chitin_meta', '0004_auto_20180922_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcegroup',
            name='current_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chitin_meta.Node'),
        ),
        migrations.AddField(
            model_name='resourcegroup',
            name='current_path',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='ghost',
            field=models.BooleanField(default=False),
        ),
    ]
