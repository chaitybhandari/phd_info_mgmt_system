from django.conf.urls import patterns, url
from phd_info_mgmt_system import views

urlpatterns = patterns('',
                       url(r'^$', views.phd_index_page,
                           name="phd_index_page"),
                       url(r'^phd_update/$', views.phd_update_page,
                           name="phd_update_page"),
                       url(r'^render_update_form/$', views.render_update_form,
                           name='phd_thesis_update'),
                       url(r'^phd_thesis_update/$', views.phd_thesis_update,
                           name='phd_thesis_update_form'),
                       url(r'^phd_insert/$', views.phd_insert_page,
                           name="phd_insert_page"),
                       url(r'^phd_scholar_insert/$', views.phd_scholar_insert,
                           name='phd_scholar_insert'),
                       url(r'^phd_scholar_update/$', views.phd_scholar_update,
                           name='phd_scholar_update'),
                       url(r'^phd_scholar_course_update/$',
                           views.phd_scholar_course_update
                           , name='phd_scholar_course_update'),
                       url(r'^phd_course_insert/$', views.phd_course_insert,
                           name='phd_course_insert'),
                       url(r'^phd_scholar_course_insert',
                           views.phd_scholar_course_insert,
                           name='phd_scholar_course_insert'),
                       url(r'^phd_qualifying_exam_update/$',
                           views.phd_scholar_qualifying_exam_update,
                           name='phd_qualifying_exam_update'),
                       url(r'^phd_scholar_profile/(?P<student_id>20\d\dPH[A-Z][A-Z]\d\d\d\dH)/$'
                           , views.render_phd_scholar_profile,
                           name='phd_scholar_profile'),
                       url(r'^phd_query_page/$'
                           , views.phd_query_page,
                           name='phd_query_page'),
                       url(r'^phd_advanced_query/$', views.render_advanced_query,
                           name='phd_advanced_query'),
                       url(r'^phd_advanced_query_filter/$',
                           views.advanced_query_filter,
                           name='phd_advanced_query_filter')
                       )
