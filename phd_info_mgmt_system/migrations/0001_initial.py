# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhDCourses',
            fields=[
                ('course_id', models.CharField(max_length=15, serialize=False, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('credits', models.IntegerField()),
            ],
            options={
                'db_table': 'phd_courses',
                'verbose_name': 'PhD Course',
                'verbose_name_plural': 'PhD Courses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhDEvaluator',
            fields=[
                ('eval_id', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('university', models.CharField(max_length=50, null=True, blank=True)),
                ('affiliation', models.CharField(max_length=50, null=True, blank=True)),
                ('other_details', models.CharField(max_length=150, null=True, blank=True)),
            ],
            options={
                'db_table': 'phd_evaluator',
                'verbose_name': 'PhD Evaluator',
                'verbose_name_plural': 'PhD Evaluators',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhDScholar',
            fields=[
                ('id_number', models.CharField(max_length=13, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('department', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=60, null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=1, null=True, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone_no', models.CharField(max_length=12, null=True, blank=True)),
                ('type', models.CharField(max_length=12, null=True, blank=True)),
                ('year_of_admission', models.CharField(max_length=7, null=True, blank=True)),
                ('semester_of_admission', models.CharField(blank=True, max_length=2, null=True, choices=[(b'I', b'First Semester'), (b'II', b'Second Semester')])),
                ('awardee_ref_no', models.CharField(max_length=20, null=True, blank=True)),
                ('fellowship_type', models.CharField(max_length=50, null=True, blank=True)),
                ('fellowship_start_date', models.DateField(null=True, verbose_name=b'Start Date', blank=True)),
                ('fellowship_end_date', models.DateField(null=True, verbose_name=b'End Date', blank=True)),
                ('total_credits', models.IntegerField(default=0, null=True, blank=True)),
            ],
            options={
                'db_table': 'phd_scholar',
                'verbose_name': 'PhD Scholar',
                'verbose_name_plural': 'PhD Scholars',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhDScholarCourses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.CharField(max_length=10)),
                ('grade', models.CharField(max_length=15, null=True, blank=True)),
                ('course_id', models.ForeignKey(to='phd_info_mgmt_system.PhDCourses')),
                ('id_number', models.ForeignKey(to='phd_info_mgmt_system.PhDScholar')),
            ],
            options={
                'db_table': 'phd_scholar_courses',
                'verbose_name': 'PhD Scholar Course',
                'verbose_name_plural': 'PhD Scholar Courses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhDThesis',
            fields=[
                ('thesis_id', models.AutoField(serialize=False, primary_key=True)),
                ('draft_submission_date', models.DateField(null=True, verbose_name=b'Draft Submission Date', blank=True)),
                ('pre_submission_date', models.DateField(null=True, verbose_name=b'Pre Submission Date', blank=True)),
                ('final_submission_date', models.DateField(null=True, verbose_name=b'Final Submission Date', blank=True)),
                ('viva_date', models.DateField(null=True, verbose_name=b'Viva Date', blank=True)),
                ('qualifying_date', models.DateField(null=True, verbose_name=b'Qualifying Date', blank=True)),
                ('phd_awarded_date', models.DateField(null=True, verbose_name=b'_(PhD Awarded Date)', blank=True)),
                ('topic_approval_status', models.CharField(max_length=3, null=True, blank=True)),
                ('research_area', models.CharField(max_length=60, null=True, blank=True)),
                ('initial_thesis_title', models.CharField(max_length=120, null=True, blank=True)),
                ('final_thesis_title', models.CharField(max_length=120, null=True, blank=True)),
                ('examiner1', models.CharField(max_length=60, null=True, blank=True)),
                ('examiner2', models.CharField(max_length=60, null=True, blank=True)),
                ('supervisor', models.CharField(max_length=60, null=True, blank=True)),
                ('dac1', models.CharField(max_length=60, null=True, blank=True)),
                ('dac2', models.CharField(max_length=60, null=True, blank=True)),
                ('cosupervisor', models.CharField(max_length=60, null=True, blank=True)),
                ('id_number', models.ForeignKey(to='phd_info_mgmt_system.PhDScholar')),
            ],
            options={
                'db_table': 'phd_thesis',
                'verbose_name': 'PhD Thesis',
                'verbose_name_plural': 'PhD Thesis',
            },
            bases=(models.Model,),
        ),
    ]
