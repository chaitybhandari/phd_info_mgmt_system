from django.template import RequestContext
from django.shortcuts import render_to_response
from phd_info_management.models import PhDScholar
# Create your views here.

def phd_scholar_form(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/phd_scholar_insert.html',
                            {}, context)


def phd_scholar_insert(request):
  context = RequestContext(request)
  if request.method == 'POST':
    request_dict = dict()
    for key in request.POST:
      if key != "csrfmiddlewaretoken":
        request_dict[key] = request.POST.get(key)
    phd_scholar = PhDScholar(**request_dict)
    phd_scholar.save()

  return render_to_response('phd_info_mgmt_system/phd_scholar_insert.html',
                            {}, context)

def phd_thesis_update_form(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/test.html',
                            {}, context)  

