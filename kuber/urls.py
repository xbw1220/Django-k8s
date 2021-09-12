from django.urls import path, re_path, include
from kuber import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path('^node/$', views.node, name="node"),
    re_path('^namespace/$', views.namespace, name="namespace"),
    re_path('^pv/$', views.pv, name="pv"),
]
