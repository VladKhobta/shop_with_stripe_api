from django.urls import path
from .views import PaymentViewSet
from rest_framework import routers

app_name = 'payments'

urlpatterns = [
    path("", PaymentViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='payments'),
]
