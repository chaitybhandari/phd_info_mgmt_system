from django.conf.urls import patterns, url
from phd_info_mgmt_system import views

urlpatterns = patterns('',
                       url(r'^phd_scholar_info/$', views.phd_scholar_form,
                           name='phd_scholar_insert'),
                       )
