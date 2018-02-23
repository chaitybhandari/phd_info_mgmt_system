# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0004_auto_20180201_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdthesis',
            name='cosupervisor',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='dac1',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='dac2',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='draft_submission_date',
            field=models.DateField(null=True, verbose_name=b'Draft Submission Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='examiner1',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='examiner2',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='final_submission_date',
            field=models.DateField(null=True, verbose_name=b'Final Submission Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='final_thesis_title',
            field=models.CharField(max_length=120, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='initial_thesis_title',
            field=models.CharField(max_length=120, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='phd_awarded_date',
            field=models.DateField(null=True, verbose_name=b'PhD Awarded Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='pre_submission_date',
            field=models.DateField(null=True, verbose_name=b'Pre Submission Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='qualifying_date',
            field=models.DateField(null=True, verbose_name=b'Qualifying Date'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='research_area',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='supervisor',
            field=models.CharField(max_length=60, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='topic_approval_status',
            field=models.CharField(max_length=3, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='viva_date',
            field=models.DateField(null=True, verbose_name=b'Viva Date'),
            preserve_default=True,
        ),
    ]
