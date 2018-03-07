# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0010_auto_20180226_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='semester',
            field=models.CharField(max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
