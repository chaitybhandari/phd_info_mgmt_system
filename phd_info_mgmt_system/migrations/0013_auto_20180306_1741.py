# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0012_auto_20180306_0654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='course_id',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDCourses', db_column=b'course_id'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='id_number',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDScholar', db_column=b'id_number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='id_number',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDScholar', db_column=b'id_number'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='scholarqualifyingexam',
            name='id_number',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDScholar', db_column=b'id_number'),
            preserve_default=True,
        ),
    ]
