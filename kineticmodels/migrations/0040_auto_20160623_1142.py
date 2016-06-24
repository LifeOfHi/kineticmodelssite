# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0039_auto_20160623_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kineticmodel',
            name='kinetics',
            field=models.ManyToManyField(blank=True, through='kineticmodels.KineticsComment', to='kineticmodels.Kinetics'),
        ),
        migrations.AlterField(
            model_name='kineticmodel',
            name='thermo',
            field=models.ManyToManyField(blank=True, through='kineticmodels.ThermoComment', to='kineticmodels.Thermo'),
        ),
        migrations.AlterField(
            model_name='kineticmodel',
            name='transport',
            field=models.ManyToManyField(blank=True, to='kineticmodels.Transport'),
        ),
    ]
