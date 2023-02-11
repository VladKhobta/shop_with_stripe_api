from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
