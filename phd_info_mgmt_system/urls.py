from django.conf.urls import patterns, url
from phd_info_mgmt_system import views

urlpatterns = patterns('',
                       url(r'^phd_scholar_info/$', views.phd_scholar_form,
                           name='phd_scholar_insert'),
                       url(r'^phd_thesis_update/$', views.phd_thesis_update_form,
                           name='phd_thesis_update'),
                       url(r'^phd_scholar_insert/$', views.phd_scholar_insert,
                           name='phd_scholar_insert')
                       )
