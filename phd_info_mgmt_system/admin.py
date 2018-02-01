from django.contrib import admin
from phd_info_mgmt_system.models import PhDScholar, PhDThesis,\
	PhDCourses, PhDScholarCourses, PhDEvaluator, ScholarQualifyingExam

# Register your models here.
admin.site.register(PhDScholar)
admin.site.register(PhDScholarCourses)
admin.site.register(PhDThesis)
admin.site.register(PhDCourses)
admin.site.register(PhDEvaluator)
admin.site.register(ScholarQualifyingExam)

