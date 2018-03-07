# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0009_auto_20180223_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdcourses',
            name='course_name',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdcourses',
            name='credits',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
