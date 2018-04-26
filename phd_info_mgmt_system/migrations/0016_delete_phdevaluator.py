# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0015_auto_20180424_2014'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PhDEvaluator',
        ),
    ]
