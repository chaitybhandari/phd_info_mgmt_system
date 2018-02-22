from django.template import RequestContext
from django.shortcuts import render_to_response
from phd_info_management.models import PhDScholar, PhDCourses

# Create your views here.

def phd_landing_page(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/index.html',
                            {}, context)

def phd_course_insert(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    for key in request.POST:
      if key != 'csrfmiddlewaretoken':
        request_dict[key] = request.POST.get(key)
    phd_course = PhDCourses(**request_dict)
    course_id = request.POST.get('course_id')
    records = PhDCourses.objects.filter(course_id=course_id)
    if len(records) > 0:
      error_msg = 'The Course with ID {id} already' \
                  ' exists in the Database.'.format(id=course_id)
      return render_to_response('phd_info_mgmt_system/phd_course_form.html',
                                {'course_exists': error_msg}, context)
    phd_course.save()
    return render_to_response('phd_info_mgmt_system/index.html', {}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_course_form.html', {}, context)

def phd_scholar_insert(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    for key in request.POST:
      if key != "csrfmiddlewaretoken":
        request_dict[key] = request.POST.get(key)
    phd_scholar = PhDScholar(**request_dict)
    id_number = request_dict.get('id_number')
    records = PhDScholar.objects.filter(id_number=id_number)
    if len(records) > 0:
      error_msg = 'The ID Number {id} already' \
                  ' exists in the Database.'.format(id=id_number)
      return render_to_response('phd_info_mgmt_system/phd_scholar_form.html',
                                {'id_number_exists': error_msg}, context)
    phd_scholar.save()
    return render_to_response('phd_info_mgmt_system/index.html', {}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_scholar_form.html',
                            {}, context)

def phd_thesis_update_form(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/phd_thesis_update.html',
                            {}, context)  

