# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0007_auto_20180222_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdthesis',
            name='id_number',
            field=models.ForeignKey(to='phd_info_mgmt_system.PhDScholar'),
            preserve_default=True,
        ),
    ]
