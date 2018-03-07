from django.template import RequestContext
from django.shortcuts import render_to_response
from phd_info_mgmt_system.models import PhDScholar, PhDCourses, PhDThesis, \
                                       PhDScholarCourses

# Create your views here.


def phd_index_page(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/index.html', {}, context)


def phd_update_page(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/phd_update.html',
                            {}, context)


def phd_insert_page(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/phd_insert.html',
                            {}, context)  


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
                                {'id_number_exists': error_msg,
                                 'form_origin': '/phd/phd_scholar_insert/'},
                                context)
    phd_scholar.save()
    success_msg = 'PhD Scholar successfully added!'
    return render_to_response('phd_info_mgmt_system/phd_insert.html', {'scholar_added': success_msg}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_scholar_form.html',
                              {'form_origin': '/phd/phd_scholar_insert/'}, context)


def phd_course_insert(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    for key in request.POST:
      if key != 'csrfmiddlewaretoken':
        request_dict[key] = request.POST.get(key)
    phd_course = PhDCourses(**request_dict)
    course_id = request_dict.get('course_id')
    records = PhDCourses.objects.filter(course_id=course_id)
    if len(records) > 0:
      error_msg = 'The Course with ID {id} already' \
                  ' exists in the Database.'.format(id=course_id)
      return render_to_response('phd_info_mgmt_system/phd_course_form.html',
                                {'course_exists': error_msg}, context)
    phd_course.save()
    success_msg = 'Course successfully added!'
    return render_to_response('phd_info_mgmt_system/phd_course_form.html', {'course_exists': success_msg}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_course_form.html', {}, context)


def phd_thesis_update(request):
  context = RequestContext(request)
  if request.method == 'POST':
    id_number = request.POST.get('id_number')
    phd_scholar_obj = PhDScholar.objects.filter(id_number=id_number)[0]
    request_dict = dict()
    for key in request.POST:
      if key != "csrfmiddlewaretoken" and key != 'source':
        if key == 'id_number':
          request_dict[key] = phd_scholar_obj
        else:
          request_dict[key] = request.POST.get(key)
    phd_thesis = PhDThesis(**request_dict)
    phd_thesis.save()
    success_msg = 'PhD Scholar Thesis Information successfully updated!'
    return render_to_response('phd_info_mgmt_system/phd_update.html',
                              {'thesis_update_success': success_msg},
                              context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_thesis_form.html'
                              , context)

def phd_scholar_course_update(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    id_number = request.POST.get('id_number')
    course_id = request.POST.get('course_id')
    phd_scholar_obj = PhDScholar.objects.filter(id_number=id_number)[0]
    course_obj = PhDCourses.objects.filter(course_id=course_id)[0]
    phd_scholar_course_list =\
     PhDScholarCourses.objects.filter(id_number=phd_scholar_obj,
                                      course_id=course_obj)
    if len(phd_scholar_course_list) > 0:
      context_dict = dict()
      error_msg = 'The Course with ID {id} and name {name} already' \
                  ' exists in the' \
                  ' Database under scholar' \
                  ' {s_id}.'.format(id=course_obj.course_id,
                                    name=course_obj.course_name,
                                    s_id=phd_scholar_obj.id_number)

      context_dict["scholar_course_exists"] = error_msg
      context_dict["form_values"] = dict()
      context_dict["form_values"]['id_number'] = phd_scholar_obj.id_number
      context_dict['dept_course_list'] = create_dept_course_list(phd_scholar_obj)
      return render_to_response('phd_info_mgmt_system/'
                                'phd_scholar_course_form.html',
                                context_dict, context)

    for key in request.POST:
      if key != "csrfmiddlewaretoken":
        if key == 'id_number':
          request_dict[key] = phd_scholar_obj
        elif key == 'course_id':
          request_dict[key] = course_obj
        else:
          request_dict[key] = request.POST.get(key)
    phd_scholar_course = PhDScholarCourses(**request_dict)
    phd_scholar_course.save()
    success_msg = "Course Information has been updated against the PhD Scholar."
    return render_to_response('phd_info_mgmt_system/phd_update.html',
                              {'scholar_update_success': success_msg}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_scholar_course_form.html',
                              {}, context)


def phd_scholar_update(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    for key in request.POST:
      if key != "csrfmiddlewaretoken":
        request_dict[key] = request.POST.get(key)
    phd_scholar = PhDScholar(**request_dict)
    phd_scholar.save()
    success_msg = 'PhD Scholar Information successfully updated!'
    return render_to_response('phd_info_mgmt_system/phd_update.html',
                              {'scholar_update_success': success_msg}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_scholar_form.html',
                              {}, context)


def render_update_form(request):
  source_resolution_dict = {
    'phd_scholar': {
        'template': 'phd_scholar_form.html',
        'class': PhDScholar
    },
    'phd_thesis': {
        'template': 'phd_thesis_form.html',
        'class': PhDThesis

    },
    'phd_qualifying': {
        'template': 'phd_qualifying_exam_form.html',
        'class': None

    },
    'phd_scholar_courses': {
        'template': 'phd_scholar_course_form.html',
        'class': PhDScholarCourses
    }
  }
  context = RequestContext(request)
  context_dict = dict()

  if request.method == 'POST':
    id_number = request.POST.get('id_number')
    source = request.POST.get('source')
    if source == "phd_scholar":
      context_dict["form_action"] = '/phd/phd_scholar_update/'
      context_dict["readonly"] = True
    records = PhDScholar.objects.filter(id_number=id_number)
    if len(records) <= 0:
      error_msg = 'The ID Number {id} does not' \
                  ' exist in the Database.'.format(id=id_number)
      return render_to_response('phd_info_mgmt_system/phd_update.html',
                                {'id_number_dn_exist': error_msg}, context)
    else:
      if source == "phd_scholar_courses":
        context_dict['dept_course_list'] = create_dept_course_list(records[0])

      source_class = ((source_resolution_dict.get(source)).get('class'))
      record_object_list = source_class.objects.filter(id_number=id_number)
      form_values = dict()
      if len(record_object_list) <= 0 or source == 'phd_scholar_courses':
        form_values['id_number'] = id_number
      else:
        record_object = record_object_list[0]
        for key in record_object.__dict__:
          if key != '_state':
            if key.endswith('_id'):
              form_values[key.rstrip('_id')] = record_object.__dict__[key]
            else:
              form_values[key] = record_object.__dict__[key]
      context_dict['form_values'] = form_values
      template = 'phd_info_mgmt_system/' \
                 '{temp}'.format(temp=source_resolution_dict.
                                 get(source).get('template'))
      return render_to_response(template, context_dict, context)


def create_dept_course_list(scholar_record):
  department_to_course_alias = {
    "Computer Science": "CS",
    "EEE": "EEE",
    "Pharmacy": "PHA",
    "Biological Sciences":"BIO",
    "Humanities and Social Sciences": "HSS"
  }
  dept_course_list = list()
  scholar_department = scholar_record.department
  scholar_courses = PhDCourses.objects.all()
  for course in scholar_courses:
    if department_to_course_alias[scholar_department] in course.course_id:
      dept_course_list.append(course)
  return dept_course_list


