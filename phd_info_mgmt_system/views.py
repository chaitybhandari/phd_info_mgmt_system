from django.template import RequestContext
from django.shortcuts import render_to_response
from phd_info_mgmt_system.models import PhDScholar, PhDCourses, PhDThesis, \
                                       PhDScholarCourses, ScholarQualifyingExam

import datetime

# Create your views here.

def phd_index_page(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/index.html', {}, context)


def phd_update_page(request):
  context = RequestContext(request)
  records = PhDScholar.objects.all()
  return render_to_response('phd_info_mgmt_system/phd_update.html',
                            {'phd_scholars': records}, context)


def phd_insert_page(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/phd_insert.html',
                            {}, context)


def phd_query_page(request):
  context = RequestContext(request)
  records = PhDScholar.objects.all()
  return render_to_response('phd_info_mgmt_system/phd_query.html',
                            {'phd_scholars': records}, context)


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


def phd_scholar_course_insert(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    id_number = request.POST.get('id_number')
    course_id = request.POST.get('course_id')
    phd_scholar_objs = PhDScholar.objects.filter(id_number=id_number)
    if len(phd_scholar_objs) <= 0:
      error_msg = "The scholar with ID {id}" \
                  " does not exist in the database.".format(id=id_number)
      courses = PhDCourses.objects.all()

      return render_to_response('phd_info_mgmt_system/'
                                'phd_scholar_course_form.html',
                                {'scholar_dn_exist': error_msg,
                                 'all_courses': courses,
                                 'disable_grades': True}, context)

    course_obj = PhDCourses.objects.filter(course_id=course_id)[0]
    phd_scholar_obj = phd_scholar_objs[0]
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
      courses = PhDCourses.objects.all()
      context_dict["all_courses"] = courses
      context_dict["disable_grades"] = True
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
    phd_params = dict()
    for key in phd_scholar_obj.__dict__:
      if key != '_state':
        if key == 'total_credits':
          phd_params[key] = phd_scholar_obj.total_credits + course_obj.credits
        else:
          phd_params[key] = phd_scholar_obj.__dict__[key]
    phd_scholar = PhDScholar(**phd_params)
    phd_scholar.save()
    success_msg = "Course Information has been updated against the PhD Scholar."
    return render_to_response('phd_info_mgmt_system/phd_insert.html',
                              {'scholar_course_added': success_msg}, context)
  else:
    courses = PhDCourses.objects.all()
    context_dict = dict()
    context_dict["form_origin"] = '/phd/phd_scholar_course_insert/'
    context_dict["all_courses"] = courses
    context_dict["disable_grades"] = True
    return render_to_response('phd_info_mgmt_system/phd_scholar_course_form.html',
                              context_dict, context)

def phd_scholar_qualifying_exam_update(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    all_phd_scholars = PhDScholar.objects.all()
    id_number = request.POST.get('id_number')
    phd_scholar_obj = PhDScholar.objects.filter(id_number=id_number)[0]
    qualifying_exam_list =\
      ScholarQualifyingExam.objects.filter(id_number=phd_scholar_obj)
    for key in request.POST:
      if key != "csrfmiddlewaretoken" and key != 'source':
        if key == 'id_number' and len(qualifying_exam_list) <= 0:
          request_dict[key] = phd_scholar_obj
        else:
          request_dict[key] = request.POST.get(key)
    if len(qualifying_exam_list) <= 0:
      phd_scholar_qualifying_exam = ScholarQualifyingExam(**request_dict)
      phd_scholar_qualifying_exam.save()
    else:
      ScholarQualifyingExam.objects.filter(id_number=
                                           phd_scholar_obj).update(**request_dict)
    success_msg = 'PhD Scholar Qualifying Exam Information successfully updated!'
    return render_to_response('phd_info_mgmt_system/phd_update.html',
                              {'update_success': success_msg,
                               'phd_scholars': all_phd_scholars},
                              context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_thesis_form.html'
                              , context)


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
    return render_to_response('phd_info_mgmt_system/phd_insert.html', {'course_added': success_msg}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_course_form.html', {}, context)


def phd_thesis_update(request):
  context = RequestContext(request)
  if request.method == 'POST':
    id_number = request.POST.get('id_number')
    all_phd_scholars = PhDScholar.objects.all()
    phd_scholar_obj = PhDScholar.objects.filter(id_number=id_number)[0]
    phd_thesis_list = PhDThesis.objects.filter(id_number=phd_scholar_obj)
    request_dict = dict()
    context_dict = dict()
    if len(phd_thesis_list) > 0:
      thesis_id = phd_thesis_list[0].thesis_id
      request_dict['thesis_id'] = thesis_id
      context_dict['set_dropdowns'] = True

    for key in request.POST:
      if key != "csrfmiddlewaretoken" and key != 'source':
        if key == 'id_number':
          request_dict[key] = phd_scholar_obj
        else:
          request_dict[key] = request.POST.get(key)
    phd_thesis = PhDThesis(**request_dict)
    phd_thesis.save()
    success_msg = 'PhD Scholar Thesis Information successfully updated!'
    context_dict['update_success'] = success_msg
    context_dict['phd_scholars'] = all_phd_scholars
    return render_to_response('phd_info_mgmt_system/phd_update.html',
                              context_dict,context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_thesis_form.html'
                              , context)

def phd_scholar_course_update(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    all_phd_scholars = PhDScholar.objects.all()
    id_number = request.POST.get('id_number')
    course_id = request.POST.get('course_id')
    phd_scholar_obj = PhDScholar.objects.filter(id_number=id_number)[0]
    course_obj = PhDCourses.objects.filter(course_id=course_id)[0]
    for key in request.POST:
      if key not in ["csrfmiddlewaretoken", "id_number", "course_id"]:
        # if key == 'id_number':
        #   request_dict[key] = phd_scholar_obj
        # elif key == 'course_id':
        #   request_dict[key] = course_obj
         request_dict[key] = request.POST.get(key)

    PhDScholarCourses.objects.filter(id_number=phd_scholar_obj,
                                     course_id=course_obj).update(**request_dict)
    # phd_scholar_course.save()
    success_msg = "Course Information has been updated against the PhD Scholar."
    return render_to_response('phd_info_mgmt_system/phd_update.html',
                              {'update_success': success_msg,
                               'phd_scholars': all_phd_scholars}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_scholar_course_form.html',
                              {}, context)


def phd_scholar_update(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    all_phd_scholars = PhDScholar.objects.all()
    for key in request.POST:
      if key != "csrfmiddlewaretoken":
        request_dict[key] = request.POST.get(key)
    phd_scholar = PhDScholar(**request_dict)
    phd_scholar.save()
    success_msg = 'PhD Scholar Information successfully updated!'

    return render_to_response('phd_info_mgmt_system/phd_update.html',
                              {'update_success': success_msg,
                               'phd_scholars': all_phd_scholars}, context)
  else:
    return render_to_response('phd_info_mgmt_system/phd_scholar_form.html',
                              {}, context)


def render_phd_scholar_profile(request, student_id):
  def render_profile(id_number):
    context_dict = dict()
    phd_scholar_obj = PhDScholar.objects.filter(id_number=id_number)[0]
    context_dict["phd_scholar"] = phd_scholar_obj

    phd_thesis_list = PhDThesis.objects.filter(id_number=phd_scholar_obj)
    if len(phd_thesis_list) > 0:
      context_dict["phd_thesis"] = phd_thesis_list[0]

    phd_scholar_courses = PhDScholarCourses.objects.filter(id_number=phd_scholar_obj)
    if len(phd_scholar_courses) > 0:
      context_dict["phd_courses"] = phd_scholar_courses

    phd_qualifying_exam_list = ScholarQualifyingExam.objects.filter(id_number=phd_scholar_obj)
    if len(phd_qualifying_exam_list) > 0:
      context_dict["phd_qualifying_exam"] = phd_qualifying_exam_list[0]
    return context_dict

  context = RequestContext(request)
  if request.method == "POST":
    id_number = request.POST.get("id_number")
    context_dict = render_profile(id_number)
    return render_to_response('phd_info_mgmt_system/phd_scholar_profile.html',
                              context_dict, context)

  else:
    id_number = student_id
    context_dict = render_profile(id_number)
    return render_to_response('phd_info_mgmt_system/phd_scholar_profile.html',
                              context_dict, context)

def render_advanced_query(request):
  context = RequestContext(request)
  scholars = PhDScholar.objects.all()
  context_dict = create_query_context_dict(scholars)
  context_dict['phd_scholars'] = scholars
  return render_to_response('phd_info_mgmt_system/phd_advanced_query.html',
                            context_dict, context)


def create_query_context_dict(scholars):
  department_list = list()
  supervisor_list = list()
  cosupervisor_list = list()
  department_supervisor_dict = dict()
  department_cosupervisor_dict = dict()
  context_dict = dict()

  for scholar in scholars:
    if scholar.department not in department_list:
      department_supervisor_dict[scholar.department] = list()
      department_cosupervisor_dict[scholar.department] = list()
      department_list.append(scholar.department)
    phd_thesis_list = PhDThesis.objects.filter(id_number=scholar)
    if len(phd_thesis_list) > 0:
      phd_thesis = phd_thesis_list[0]
      if phd_thesis.supervisor:
        if phd_thesis.supervisor not in supervisor_list:
          supervisor_list.append(phd_thesis.supervisor)
        if phd_thesis.supervisor\
           not in department_supervisor_dict[scholar.department]:
          department_supervisor_dict[scholar.department].append(phd_thesis.supervisor)
      if phd_thesis.cosupervisor:
        if phd_thesis.cosupervisor not in cosupervisor_list:
          cosupervisor_list.append(phd_thesis.cosupervisor)
        if phd_thesis.cosupervisor\
           not in department_cosupervisor_dict[scholar.department]:
          department_cosupervisor_dict[scholar.department].append(phd_thesis.cosupervisor)
  context_dict['department_list'] = department_list
  context_dict['dept_supervisor_dict'] = department_supervisor_dict
  context_dict['dept_cosupervisor_dict'] = department_cosupervisor_dict
  context_dict['supervisor_list'] = supervisor_list
  context_dict['cosupervisor_list'] = cosupervisor_list
  context_dict['all_courses'] = PhDCourses.objects.all()
  return context_dict


def advanced_query_filter(request):

  context = RequestContext(request)
  if request.method == 'POST':
    query_dict = dict()
    form_values = dict()
    for key in request.POST:
      if key != "csrfmiddlewaretoken":
        form_values[key] = request.POST.get(key)
        if key.startswith('phd_scholar_course_'):
          if not query_dict.get(PhDScholarCourses):
            query_dict[PhDScholarCourses] = dict()
          actual_key = key[len('phd_scholar_course_'):]
          if 'course_id' in key:
            query_dict[PhDScholarCourses][actual_key] =\
              PhDCourses.objects.filter(course_id=request.POST.get(key))[0]
          query_dict[PhDScholarCourses][actual_key] = request.POST.get(key)
        elif key.startswith('phd_scholar_'):
          if not query_dict.get(PhDScholar):
            query_dict[PhDScholar] = dict()
          actual_key = key[len('phd_scholar_'):]
          query_dict[PhDScholar][actual_key] = request.POST.get(key)
        elif key.startswith('phd_thesis_'):
          if not query_dict.get(PhDThesis):
            query_dict[PhDThesis] = dict()
          actual_key = key[len('phd_thesis_'):]
          query_dict[PhDThesis][actual_key] = request.POST.get(key)

    for cls, attr_dict in query_dict.iteritems():
      if cls in [PhDThesis, PhDScholarCourses]:
        filtered_list = cls.objects.filter(**attr_dict)
        id_number_list = [element.id_number for element in filtered_list]
        query_dict[cls]['filtered_list'] = id_number_list
      else:
        query_dict[cls]['filtered_list'] = cls.objects.filter(**attr_dict)
    query_list = list()
    for cls in query_dict:
      query_list.append(set(query_dict[cls].get('filtered_list')))

    scholars = PhDScholar.objects.all()
    final_id_number_list = set.intersection(*query_list)
    context_dict = create_query_context_dict(scholars)
    context_dict["phd_scholars"] = final_id_number_list
    context_dict["form_values"] = form_values
    context_dict["set_dropdowns"] = True
    return render_to_response('phd_info_mgmt_system/phd_advanced_query.html',
                              context_dict, context)

def render_update_form(request):
  source_resolution_dict = {
    'phd_scholar': {
        'template': 'phd_scholar_form.html',
        'class': PhDScholar,
        'url': '/phd/phd_scholar_update/'
    },
    'phd_thesis': {
        'template': 'phd_thesis_form.html',
        'class': PhDThesis

    },
    'phd_qualifying': {
        'template': 'phd_scholar_qualifying_exam_form.html',
        'class': ScholarQualifyingExam,
        'url': '/phd/phd_qualifying_exam_update/'
    },
    'phd_scholar_courses': {
        'template': 'phd_scholar_course_form.html',
        'class': PhDScholarCourses,
        'url': '/phd/phd_scholar_course_update/'
    }
  }
  context = RequestContext(request)
  context_dict = dict()

  if request.method == 'POST':
    id_number = request.POST.get('id_number')
    phd_scholar_list = PhDScholar.objects.filter(id_number=id_number)
    phd_scholar_obj = phd_scholar_list[0]
    source = request.POST.get('source')
    all_phd_scholars = PhDScholar.objects.all()

    if source in ["phd_scholar", "phd_scholar_courses"]:
      context_dict["form_action"] = source_resolution_dict[source]["url"]
      context_dict["readonly"] = True

    if len(phd_scholar_list) <= 0:
      error_msg = 'The ID Number {id} does not' \
                  ' exist in the Database.'.format(id=id_number)

      return render_to_response('phd_info_mgmt_system/phd_update.html',
                                {'id_number_dn_exist': error_msg,
                                 'phd_scholars': all_phd_scholars}, context)
    else:
      if source == "phd_scholar_courses":
        scholar_course_records =\
          PhDScholarCourses.objects.filter(id_number=phd_scholar_obj)
        if len(scholar_course_records) <= 0:
          error_msg = "There are no courses registered" \
                      " under the student " \
                      "with ID {id}.".format(id=phd_scholar_obj.id_number)
          return render_to_response('phd_info_mgmt_system/phd_update.html',
                                    {'no_scholar_courses': error_msg,
                                     'phd_scholars': all_phd_scholars}, context)
        scholar_course_info = dict()
        scholar_course_records = PhDScholarCourses.objects.filter(id_number=phd_scholar_obj)
        for scholar_course in scholar_course_records:
          if not scholar_course_info.get(scholar_course.course_id.course_id):
            scholar_course_info[scholar_course.course_id.course_id] = dict()
          scholar_course_info[scholar_course.course_id.course_id]["course_year"] = scholar_course.course_year
          scholar_course_info[scholar_course.course_id.course_id]["semester"] = scholar_course.semester
          scholar_course_info[scholar_course.course_id.course_id]["grade"] = scholar_course.grade

        context_dict['scholar_course_info'] = scholar_course_info
        context_dict['scholar_course_list'] = create_scholar_course_list(phd_scholar_obj)

      elif source == "phd_thesis":
        phd_exam_list = \
          ScholarQualifyingExam.objects.filter(id_number=phd_scholar_obj)

        if len(phd_exam_list) <= 0:
          error_msg = 'The student with ID {id} has not ' \
                      'appeared for the qualifying exam yet.'.format(id=id_number)
          return render_to_response('phd_info_mgmt_system/phd_update.html',
                                    {'no_qualifying_exam': error_msg,
                                     'phd_scholars': all_phd_scholars}, context)
        else:
          scholar_exam_obj = phd_exam_list[0]
          result = scholar_exam_obj.final_result
          if result in ['Fail', None]:
            error_msg = 'Cannot update thesis information for student' \
                        ' with ID {id}, since the' \
                        ' Qualifying Exam has not been passed.'.format(id=id_number)
            return render_to_response('phd_info_mgmt_system/phd_update.html',
                                      {'qualifying_exam_fail': error_msg,
                                       'phd_scholars': all_phd_scholars}, context)

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
            elif 'date' in key:
              if record_object.__dict__[key]:
                form_values[key] = record_object.__dict__[key].strftime('%Y-%m-%d')
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
    "Biological Sciences" : "BIO",
    "Humanities and Social Sciences": "HSS"
  }
  dept_course_list = list()
  scholar_department = scholar_record.department
  scholar_courses = PhDCourses.objects.all()
  for course in scholar_courses:
    if department_to_course_alias[scholar_department] in course.course_id:
      dept_course_list.append(course)
  return dept_course_list


def create_scholar_course_list(scholar_record):
  records = PhDScholarCourses.objects.filter(id_number=scholar_record)
  scholar_course_list =\
    [scholar_course.course_id for scholar_course in records]
  return scholar_course_list

# //.filter-form {
# //    display: inline-block;
# //   width: 70%;
# //}
#
# //.searchable-list {
# //    display: inline-block;
# //    float: right;
# //    width: 30%;
#
# //  }
