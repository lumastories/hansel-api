from django.conf.urls import url, include
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^docs/', include('rest_framework_docs.urls')),
]
