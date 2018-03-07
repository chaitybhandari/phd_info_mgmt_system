# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0011_auto_20180306_0651'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='phdscholarcourses',
            unique_together=set([('id_number', 'course_id')]),
        ),
    ]
