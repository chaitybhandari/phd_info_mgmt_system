# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0002_auto_20180123_0509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phdscholar',
            old_name='ID',
            new_name='id_number',
        ),
        migrations.RenameField(
            model_name='phdthesis',
            old_name='ID',
            new_name='id_number',
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='awardee_ref_no',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='email',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_end_date',
            field=models.DateField(null=True, verbose_name=b'_(End Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_start_date',
            field=models.DateField(null=True, verbose_name=b'_(Start Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_type',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='phone_no',
            field=models.CharField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='semester_of_admission',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[(b'I', b'First Semester'), (b'II', b'Second Semester')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='total_credits',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='type',
            field=models.CharField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='year_of_admission',
            field=models.CharField(max_length=7, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='draft_submission_date',
            field=models.DateField(null=True, verbose_name=b'_(Draft Submission Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='examiner1',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='examiner2',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='final_submission_date',
            field=models.DateField(null=True, verbose_name=b'_(Final Submission Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='final_thesis_title',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='initial_thesis_title',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='phd_awarded_date',
            field=models.DateField(null=True, verbose_name=b'_(PhD Awarded Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='pre_submission_date',
            field=models.DateField(null=True, verbose_name=b'_(Pre Submission Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='qualifying_date',
            field=models.DateField(null=True, verbose_name=b'_(Qualifying Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='research_area',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='supervisor',
            field=models.CharField(max_length=60, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='topic_approval_status',
            field=models.CharField(max_length=3, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='viva_date',
            field=models.DateField(null=True, verbose_name=b'_(Viva Date)', blank=True),
            preserve_default=True,
        ),
    ]
