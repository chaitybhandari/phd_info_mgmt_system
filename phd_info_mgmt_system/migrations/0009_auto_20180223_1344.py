# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0008_auto_20180222_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='course_id',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDCourses'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='id_number',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDScholar'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scholarqualifyingexam',
            name='id_number',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDScholar'),
            preserve_default=True,
        ),
    ]
