from django.contrib import admin
from phd_info_mgmt_system.models import PhDScholar, PhDThesis,\
  PhDCourses, PhDScholarCourses, ScholarQualifyingExam

class PhDScholarAdmin(admin.ModelAdmin):
  list_display = ('id_number', 'name', 'department')

class PhDThesisAdmin(admin.ModelAdmin):
  list_display = ('id_number', 'get_name', 'research_area', 'supervisor')

  def get_name(self, obj):
    return obj.id_number.name
  get_name.short_description = "Scholar Name"


class PhDScholarCoursesAdmin(admin.ModelAdmin):
  list_display = ('id_number', 'get_scholar_name',
                  'get_course_id', 'get_course_name')

  def get_scholar_name(self, obj):
    return obj.id_number.name
  get_scholar_name.short_description = "Scholar Name"

  def get_course_name(self,obj):
    return obj.course_id.course_name
  get_course_name.short_description = "Course Name"

  def get_course_id(self, obj):
    return obj.course_id.course_id
  get_course_id.short_description = "Course ID"

class PhDCoursesAdmin(admin.ModelAdmin):
  list_display = ('course_id', 'course_name', 'credits')


class ScholarQualifyingExamAdmin(admin.ModelAdmin):
  list_display = ('id_number', 'final_result')


# Register your models here.
admin.site.register(PhDScholar, PhDScholarAdmin)
admin.site.register(PhDScholarCourses, PhDScholarCoursesAdmin)
admin.site.register(PhDThesis, PhDThesisAdmin)
admin.site.register(PhDCourses, PhDCoursesAdmin)
admin.site.register(ScholarQualifyingExam, ScholarQualifyingExamAdmin)



