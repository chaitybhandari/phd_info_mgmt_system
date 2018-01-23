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
                ('course_name', models.CharField(default=None, max_length=50)),
                ('credits', models.IntegerField(default=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhDEvaluator',
            fields=[
                ('evalID', models.CharField(max_length=11, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('university', models.CharField(default=None, max_length=50)),
                ('affiliation', models.CharField(default=None, max_length=50)),
                ('other_details', models.CharField(default=None, max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhDScholar',
            fields=[
                ('ID', models.CharField(max_length=12, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('department', models.CharField(max_length=50)),
                ('email', models.CharField(default=None, max_length=60)),
                ('gender', models.CharField(default=None, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('phone_no', models.CharField(default=None, max_length=12)),
                ('type', models.CharField(default=None, max_length=12)),
                ('year_of_admission', models.CharField(default=None, max_length=7)),
                ('semester_of_admission', models.CharField(max_length=2, choices=[(b'I', b'First Semester'), (b'II', b'Second Semester')])),
                ('awardee_ref_no', models.CharField(max_length=20)),
                ('fellowship_type', models.CharField(default=None, max_length=50)),
                ('fellowship_start_date', models.DateField(default=None, verbose_name=b'_(Start Date)')),
                ('fellowship_end_date', models.DateField(default=None, verbose_name=b'_(End Date)')),
                ('total_credits', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhdScholarCourses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.CharField(max_length=10)),
                ('grade', models.CharField(default=None, max_length=15)),
                ('ID', models.ForeignKey(to='phd_info_management.PhDScholar')),
                ('course_id', models.ForeignKey(to='phd_info_management.PhDCourses')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PhDThesis',
            fields=[
                ('thesis_id', models.AutoField(serialize=False, primary_key=True)),
                ('draft_submission_date', models.DateField(default=None, verbose_name=b'_(Draft Submission Date)')),
                ('pre_submission_date', models.DateField(default=None, verbose_name=b'_(Pre Submission Date)')),
                ('final_submission_date', models.DateField(default=None, verbose_name=b'_(Final Submission Date)')),
                ('viva_date', models.DateField(default=None, verbose_name=b'_(Viva Date)')),
                ('qualifying_date', models.DateField(default=None, verbose_name=b'_(Qualifying Date)')),
                ('phd_awarded_date', models.DateField(default=None, verbose_name=b'_(PhD Awarded Date)')),
                ('topic_approval_status', models.CharField(default=None, max_length=3)),
                ('research_area', models.CharField(default=None, max_length=60)),
                ('initial_thesis_title', models.CharField(default=None, max_length=120)),
                ('final_thesis_title', models.CharField(default=None, max_length=120)),
                ('examiner1', models.CharField(default=None, max_length=60)),
                ('examiner2', models.CharField(default=None, max_length=60)),
                ('supervisor', models.CharField(default=None, max_length=60)),
                ('DAC1', models.CharField(default=None, max_length=60)),
                ('DAC2', models.CharField(default=None, max_length=60)),
                ('cosupervisor', models.CharField(default=None, max_length=60)),
                ('ID', models.ForeignKey(to='phd_info_management.PhDScholar')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
