from django.contrib import admin
from phd_info_mgmt_system.models import PhDScholar, PhDThesis,\
  PhDCourses, PhDScholarCourses, PhDEvaluator, ScholarQualifyingExam

class PhDScholarAdmin(admin.ModelAdmin):
  list_display = ('id_number', 'name', 'department')


# Register your models here.
admin.site.register(PhDScholar, PhDScholarAdmin)
admin.site.register(PhDScholarCourses)
admin.site.register(PhDThesis)
admin.site.register(PhDCourses)
admin.site.register(PhDEvaluator)
admin.site.register(ScholarQualifyingExam)



