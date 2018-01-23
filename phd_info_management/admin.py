from django.contrib import admin
from phd_info_management.models import PhDScholar, PhDThesis,\
	PhDCourses, PhDScholarCourses

# Register your models here.
admin.site.register(PhDScholar)
admin.site.register(PhDScholarCourses)
admin.site.register(PhDThesis)
admin.site.register(PhDCourses)

