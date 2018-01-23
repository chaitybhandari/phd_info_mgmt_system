# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0003_auto_20180123_0522'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phdevaluator',
            old_name='evalID',
            new_name='eval_id',
        ),
        migrations.RenameField(
            model_name='phdscholarcourses',
            old_name='ID',
            new_name='id_number',
        ),
        migrations.RemoveField(
            model_name='phdthesis',
            name='DAC1',
        ),
        migrations.RemoveField(
            model_name='phdthesis',
            name='DAC2',
        ),
        migrations.AddField(
            model_name='phdthesis',
            name='dac1',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phdthesis',
            name='dac2',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdevaluator',
            name='affiliation',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdevaluator',
            name='other_details',
            field=models.CharField(max_length=150, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdevaluator',
            name='university',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='grade',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='cosupervisor',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
    ]
