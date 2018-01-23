# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phdcourses',
            name='course_name',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdcourses',
            name='credits',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdevaluator',
            name='affiliation',
            field=models.CharField(default=None, max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdevaluator',
            name='other_details',
            field=models.CharField(default=None, max_length=150, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdevaluator',
            name='university',
            field=models.CharField(default=None, max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='awardee_ref_no',
            field=models.CharField(max_length=20, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='email',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_end_date',
            field=models.DateField(default=None, verbose_name=b'_(End Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_start_date',
            field=models.DateField(default=None, verbose_name=b'_(Start Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='fellowship_type',
            field=models.CharField(default=None, max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='gender',
            field=models.CharField(default=None, max_length=1, blank=True, choices=[(b'M', b'Male'), (b'F', b'Female')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='phone_no',
            field=models.CharField(default=None, max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='semester_of_admission',
            field=models.CharField(blank=True, max_length=2, choices=[(b'I', b'First Semester'), (b'II', b'Second Semester')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='total_credits',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='type',
            field=models.CharField(default=None, max_length=12, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholar',
            name='year_of_admission',
            field=models.CharField(default=None, max_length=7, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdscholarcourses',
            name='grade',
            field=models.CharField(default=None, max_length=15, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='DAC1',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='DAC2',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='cosupervisor',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='draft_submission_date',
            field=models.DateField(default=None, verbose_name=b'_(Draft Submission Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='examiner1',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='examiner2',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='final_submission_date',
            field=models.DateField(default=None, verbose_name=b'_(Final Submission Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='final_thesis_title',
            field=models.CharField(default=None, max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='initial_thesis_title',
            field=models.CharField(default=None, max_length=120, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='phd_awarded_date',
            field=models.DateField(default=None, verbose_name=b'_(PhD Awarded Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='pre_submission_date',
            field=models.DateField(default=None, verbose_name=b'_(Pre Submission Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='qualifying_date',
            field=models.DateField(default=None, verbose_name=b'_(Qualifying Date)', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='research_area',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='supervisor',
            field=models.CharField(default=None, max_length=60, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='topic_approval_status',
            field=models.CharField(default=None, max_length=3, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='viva_date',
            field=models.DateField(default=None, verbose_name=b'_(Viva Date)', blank=True),
            preserve_default=True,
        ),
    ]
