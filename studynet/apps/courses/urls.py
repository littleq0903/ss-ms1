from django.conf.urls.defaults import *

from django.views.generic import TemplateView

urlpatterns = patterns('courses.views',
    url(r'^update/batch/$', 'batch_update'),
    url(r'^depart-(?P<depart_id>\w+)/$', 'all_course_page', name="all-course-page"),
    url(r'^course-(?P<course_id>\w+)/$', 'course_detail', name="course-detail-page"),
    url(r'^(?P<school>\w+)/(?P<course_id>\w+)/$', 'forward'),
    url(r'^$', 'all_course_page'),
)

urlpatterns += patterns('courses.ajax',
    # query by department
    url(r'^ajax/by_depart/(?P<depart_id>\w+)/$', 'query_course_by_department'),
    url(r'^ajax/by_depart/(?P<depart_id>\w+)/(?P<limit>\d+)/$', 'query_course_by_department'),
    url(r'^ajax/by_depart/(?P<depart_id>\w+)/(?P<limit>\d+)/(?P<offset>\d+)/$', 'query_course_by_department'),
    # query course detail
    url(r'^ajax/detail/(?P<course_id>\w+)/$', 'query_course_detail')
)
