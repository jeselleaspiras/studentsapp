from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('appuser.urls')),
    url(r'', include('studentsapp.urls')),
    url(r'^api/studentsapp/', include('studentsapp.api.urls', namespace='studentsapp-api')),
]
