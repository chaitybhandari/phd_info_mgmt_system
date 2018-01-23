# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0006_auto_20180123_0606'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='phdcourses',
            table='phd_courses',
        ),
        migrations.AlterModelTable(
            name='phdevaluator',
            table='phd_evaluator',
        ),
        migrations.AlterModelTable(
            name='phdscholar',
            table='phd_scholar',
        ),
        migrations.AlterModelTable(
            name='phdscholarcourses',
            table='phd_scholar_courses',
        ),
        migrations.AlterModelTable(
            name='phdthesis',
            table='phd_thesis',
        ),
    ]
