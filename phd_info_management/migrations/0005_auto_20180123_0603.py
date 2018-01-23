# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0004_auto_20180123_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdscholar',
            name='id_number',
            field=models.CharField(max_length=13, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
