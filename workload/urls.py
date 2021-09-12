from django.urls import path, re_path, include
from workload import views

urlpatterns = [
    re_path('^deployment/$', views.deployment, name="deployment"),
    re_path('^daemonset/$', views.daemonset, name="daemonset"),
    re_path('^statefulset/$', views.statefulset, name="statefulset"),
    re_path('^pods/$', views.pods, name="pods"),
    re_path('^cronjobs/$', views.cronjobs, name="cronjobs"),
    re_path('^jobs/$', views.jobs, name="jobs"),
]
