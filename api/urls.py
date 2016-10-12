from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'location', views.LocationViewSet, base_name='location')
router.register(r'photo', views.PhotoViewSet, base_name='photo')
router.register(r'participant', views.ParticipantViewSet, base_name='participant')
router.register(r'record', views.RecordViewSet, base_name='record')

urlpatterns = router.urls