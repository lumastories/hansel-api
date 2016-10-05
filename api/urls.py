from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'feedingprogram', views.FeedingProgramViewSet, base_name='feedingprogram')


urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += router.urls