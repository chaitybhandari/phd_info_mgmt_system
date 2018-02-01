from django.template import RequestContext
from django.shortcuts import render_to_response
# Create your views here.

def phd_scholar_form(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/phd_scholar_insert.html',
                            {}, context)

def phd_thesis_update_form(request):
  context = RequestContext(request)
  return render_to_response('phd_info_mgmt_system/test.html',
                            {}, context)  

