from django.conf.urls import re_path
from .import views
from django.urls import re_path as url

urlpatterns = [
    # url(r'^$', ,),
    url(r'^resumefill', views.resumeFill, name='resume_fill'),
    url(r'^resumeview', views.resumeView, name='resume_view'),


]
