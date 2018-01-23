# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0005_auto_20180123_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_end_date',
            field=models.DateField(null=True, verbose_name=b'End Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_start_date',
            field=models.DateField(null=True, verbose_name=b'Start Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='draft_submission_date',
            field=models.DateField(null=True, verbose_name=b'Draft Submission Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='final_submission_date',
            field=models.DateField(null=True, verbose_name=b'Final Submission Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='pre_submission_date',
            field=models.DateField(null=True, verbose_name=b'Pre Submission Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='qualifying_date',
            field=models.DateField(null=True, verbose_name=b'Qualifying Date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='viva_date',
            field=models.DateField(null=True, verbose_name=b'Viva Date', blank=True),
            preserve_default=True,
        ),
    ]
