# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-11 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kineticmodels', '0046_auto_20160811_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transport',
            old_name='dipole_moment',
            new_name='dipoleMoment',
        ),
        migrations.RenameField(
            model_name='transport',
            old_name='potential_well_depth',
            new_name='potentialWellDepth',
        ),
    ]
