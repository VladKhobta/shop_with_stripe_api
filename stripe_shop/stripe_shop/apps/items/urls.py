from django.urls import path
from .views import ItemViewSet
from rest_framework import routers

app_name = 'items'

router = routers.DefaultRouter()
router.register(r'', ItemViewSet, basename='item')

urlpatterns = router.urls
