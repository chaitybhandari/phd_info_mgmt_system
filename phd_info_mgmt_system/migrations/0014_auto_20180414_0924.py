# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0013_auto_20180306_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarqualifyingexam',
            name='id',
        ),
        migrations.AlterField(
            model_name='scholarqualifyingexam',
            name='id_number',
            field=models.ForeignKey(primary_key=True, db_column=b'id_number', serialize=False, to='phd_info_mgmt_system.PhDScholar'),
            preserve_default=True,
        ),
    ]
