from django.conf.urls import url, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [

    #url(r'^$', RedirectView.as_view(url='/home', permanent=False)),
    url(r'^$', views.login_view, name='home'),
    url(r'^login/$', RedirectView.as_view(url='/home', permanent=False)),

    url(r'^register/', views.register_view, name='register'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^', include("studentsapp.urls", namespace='posts')),
]

