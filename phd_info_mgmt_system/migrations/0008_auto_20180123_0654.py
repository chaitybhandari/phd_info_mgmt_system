# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0007_auto_20180123_0615'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phdcourses',
            options={'verbose_name': 'phd_courses'},
        ),
        migrations.AlterModelOptions(
            name='phdscholar',
            options={'verbose_name': 'phd_scholar'},
        ),
        migrations.AlterModelOptions(
            name='phdscholarcourses',
            options={'verbose_name': 'phd_scholar_courses'},
        ),
        migrations.AlterModelOptions(
            name='phdthesis',
            options={'verbose_name': 'phd_thesis'},
        ),
    ]
