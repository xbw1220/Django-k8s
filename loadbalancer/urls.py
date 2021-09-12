from django.urls import path, re_path, include
from loadbalancer import views

urlpatterns = [
    re_path('^service/$', views.service, name="service"),
    re_path('^ingress/$', views.ingress, name="ingress")
]
