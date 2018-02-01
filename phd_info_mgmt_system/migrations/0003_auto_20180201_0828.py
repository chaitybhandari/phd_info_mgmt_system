# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0002_auto_20180124_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phdscholar',
            old_name='gender',
            new_name='sex',
        ),
    ]
