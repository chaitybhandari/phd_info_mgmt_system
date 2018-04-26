# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0014_auto_20180414_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='phdscholarcourses',
            name='course_year',
            field=models.CharField(default=2018, max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='semester',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
