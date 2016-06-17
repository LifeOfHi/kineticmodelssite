# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 22:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0029_auto_20150727_1435'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='KinModel',
            new_name='KineticModel',
        ),
        migrations.RenameModel(
            old_name='SpecName',
            new_name='SpeciesName',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='kinmodel',
            new_name='kineticModel',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='jour_vol_num',
            new_name='journal_volume_number',
        ),
        migrations.RenameField(
            model_name='source',
            old_name='pub_year',
            new_name='publication_year',
        ),
        migrations.RenameField(
            model_name='species',
            old_name='CAS',
            new_name='cas',
        ),
        migrations.RenameField(
            model_name='thermocomment',
            old_name='kinmodel',
            new_name='kineticModel',
        ),
    ]
