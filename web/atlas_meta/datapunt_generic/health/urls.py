from django.conf.urls import url

from . import views

app_name = 'datapunt-health'

urlpatterns = [
    url(r'^health$', views.health),
    url(r'^data$', views.check_data),
]
