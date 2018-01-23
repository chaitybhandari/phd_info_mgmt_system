from django.db import models


class PhDScholar(models.Model):
  GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
  )
  SEMESTER_CHOICES = (
    ('I', 'First Semester'),
    ('II', 'Second Semester')
  )
  id_number = models.CharField(max_length=13, primary_key=True)
  name = models.CharField(max_length=60)
  department = models.CharField(max_length=50)
  email = models.CharField(max_length=60, null=True, blank=True)
  gender = models.CharField(max_length=1, null=True,
                            choices=GENDER_CHOICES, blank=True)
  phone_no = models.CharField(max_length=12, null=True, blank=True)
  type = models.CharField(max_length=12, null=True, blank=True)
  year_of_admission = models.CharField(max_length=7, null=True, blank=True)
  semester_of_admission = models.CharField(max_length=2,
                                           choices=SEMESTER_CHOICES,
                                           null=True, blank=True)
  awardee_ref_no = models.CharField(max_length=20, null=True, blank=True)
  fellowship_type = models.CharField(max_length=50, null=True, blank=True)
  fellowship_start_date = models.DateField("Start Date",
                                           null=True, blank=True)
  fellowship_end_date = models.DateField("End Date",
                                         null=True, blank=True)
  total_credits = models.IntegerField(default=0, blank=True, null=True)

  def __unicode__(self):
    return self.id_number

  class Meta:
    db_table = "phd_scholar"
    verbose_name = "PhD Scholar"
    verbose_name_plural = "PhD Scholars"

class PhDThesis(models.Model):
  thesis_id = models.AutoField(primary_key=True)
  id_number = models.ForeignKey(PhDScholar, on_delete=models.CASCADE)
  draft_submission_date = models.DateField("Draft Submission Date",
                                           null=True, blank=True)
  pre_submission_date = models.DateField("Pre Submission Date",
                                         null=True, blank=True)
  final_submission_date = models.DateField("Final Submission Date",
                                           null=True, blank=True)
  viva_date = models.DateField("Viva Date", null=True, blank=True)
  qualifying_date = models.DateField("Qualifying Date",
                                     null=True, blank=True)
  phd_awarded_date = models.DateField("_(PhD Awarded Date)",
                                      null=True, blank=True)
  topic_approval_status = models.CharField(max_length=3,
                                           null=True, blank=True)
  research_area = models.CharField(max_length=60, null=True, blank=True)
  initial_thesis_title = models.CharField(max_length=120,
                                          null=True, blank=True)
  final_thesis_title = models.CharField(max_length=120,
                                        null=True, blank=True)
  examiner1 = models.CharField(max_length=60, null=True, blank=True)
  examiner2 = models.CharField(max_length=60, null=True, blank=True)
  supervisor = models.CharField(max_length=60, null=True, blank=True)
  dac1 = models.CharField(max_length=60, null=True, blank=True)
  dac2 = models.CharField(max_length=60, null=True, blank=True)
  cosupervisor = models.CharField(max_length=60, null=True, blank=True)

  class Meta:
    db_table = "phd_thesis"
    verbose_name = "PhD Thesis"
    verbose_name_plural = "PhD Thesis"


class PhDCourses(models.Model):
  course_id = models.CharField(max_length=15, primary_key=True)
  course_name = models.CharField(max_length=50)
  credits = models.IntegerField()

  class Meta:
    db_table = "phd_courses"
    verbose_name = "PhD Course"
    verbose_name_plural = "PhD Courses"

class PhDScholarCourses(models.Model):
  id_number = models.ForeignKey(PhDScholar, on_delete=models.CASCADE)
  course_id = models.ForeignKey(PhDCourses, on_delete=models.CASCADE)
  semester = models.CharField(max_length=10)
  grade = models.CharField(max_length=15, null=True, blank=True)

  class Meta:
    db_table = "phd_scholar_courses"
    verbose_name = "PhD Scholar Course"
    verbose_name_plural = "PhD Scholar Courses"


class PhDEvaluator(models.Model):
  eval_id = models.CharField(max_length=11, primary_key=True)
  name = models.CharField(max_length=60)
  university = models.CharField(max_length=50, null=True, blank=True)
  affiliation = models.CharField(max_length=50, null=True, blank=True)
  other_details = models.CharField(max_length=150, null=True, blank=True)

  class Meta:
    db_table = "phd_evaluator"






