from django.conf.urls import url

from . import views

app_name = 'schedule'

urlpatterns = [
    url(r'^$', views.schedule, name='schedule'),
    url(r'^upload/$', views.upload_schedule, name='schedule_upload'),
]