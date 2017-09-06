from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^students/$', views.post_list, name='post_list'),
    url(r'^students/create/$', views.post_create, name='post_create'),
    url(r'^students/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^students/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    url(r'^students/accounts/$', views.student_list, name='student_list'),
    url(r'^students/accounts/create/$', views.student_create, name='student_create'),
    url(r'^students/accounts/(?P<pk>\d+)/edit/$', views.student_edit, name='student_edit'),
    url(r'^students/accounts/(?P<pk>\d+)/delete/$', views.student_delete, name='student_delete'),
]
