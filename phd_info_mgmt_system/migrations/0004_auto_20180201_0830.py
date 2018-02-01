# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0003_auto_20180201_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phdscholar',
            old_name='type',
            new_name='phd_type',
        ),
    ]
