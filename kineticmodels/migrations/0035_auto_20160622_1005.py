# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-22 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0034_auto_20160617_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kineticmodel',
            name='source',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='kineticmodels.Source'),
        ),
    ]
