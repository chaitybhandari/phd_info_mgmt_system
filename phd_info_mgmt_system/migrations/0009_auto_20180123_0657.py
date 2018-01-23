# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0008_auto_20180123_0654'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phdcourses',
            options={'verbose_name': 'PhD Course', 'verbose_name_plural': 'PhD Courses'},
        ),
        migrations.AlterModelOptions(
            name='phdscholar',
            options={'verbose_name': 'PhD Scholar', 'verbose_name_plural': 'PhD Scholars'},
        ),
        migrations.AlterModelOptions(
            name='phdscholarcourses',
            options={'verbose_name': 'PhD Scholar Course', 'verbose_name_plural': 'PhD Scholar Courses'},
        ),
        migrations.AlterModelOptions(
            name='phdthesis',
            options={'verbose_name': 'PhD Thesis', 'verbose_name_plural': 'PhD Thesis'},
        ),
    ]
