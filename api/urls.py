from django.conf.urls import url, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'feedingprogram', views.FeedingProgramViewSet, base_name='feedingprogram')

urlpatterns = router.urls