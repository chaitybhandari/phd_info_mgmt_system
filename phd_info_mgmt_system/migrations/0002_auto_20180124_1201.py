# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phd_info_mgmt_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarQualifyingExam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('primary_area', models.CharField(max_length=60, null=True, blank=True)),
                ('secondary_area', models.CharField(max_length=60, null=True, blank=True)),
                ('first_attempt_date', models.DateField(null=True, verbose_name=b'First Attempt Date', blank=True)),
                ('second_attempt_date', models.DateField(null=True, verbose_name=b'Second Attempt Date', blank=True)),
                ('final_result', models.CharField(max_length=60, null=True, blank=True)),
                ('id_number', models.ForeignKey(to='phd_info_mgmt_system.PhDScholar')),
            ],
            options={
                'db_table': 'scholar_qualifying_exam',
                'verbose_name': 'Scholar Qualifying Exam',
                'verbose_name_plural': 'Scholar Qualifying Exam',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='phdthesis',
            name='phd_awarded_date',
            field=models.DateField(null=True, verbose_name=b'PhD Awarded Date', blank=True),
            preserve_default=True,
        ),
    ]
