from django.urls import path, re_path, include
from storage import views

urlpatterns = [
    re_path('^pvc/$', views.pvc, name="pvc"),
    re_path('^configmap/$', views.configmap, name="configmap"),
    re_path('^secret/$', views.secret, name="secret"),
]
