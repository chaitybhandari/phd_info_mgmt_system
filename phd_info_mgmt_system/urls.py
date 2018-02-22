from django.conf.urls import patterns, url
from phd_info_mgmt_system import views

urlpatterns = patterns('',
                       url(r'^$', views.phd_landing_page,
                           name="phd_landing_page"),
                       url(r'^phd_thesis_update/$', views.phd_thesis_update_form,
                           name='phd_thesis_update'),
                       url(r'^phd_scholar_insert/$', views.phd_scholar_insert,
                           name='phd_scholar_insert'),
                       url(r'^phd_course_insert/$', views.phd_course_insert,
                           name='phd_course_insert'),
                       )
