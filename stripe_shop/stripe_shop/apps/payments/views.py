import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Payment
from .serializers import PaymentSerializer
from ..items.models import Item
import stripe
from .. import settings
# Create your views here.
from django.http import JsonResponse


# @csrf_exempt
# def create_payment_intent(request, pk):
#
#     request_data = json.loads(request.body)
#     item = get_object_or_404(Item, pk=pk)
#
#     # currency = request_data.currency
#     # price_value = item.price if currency == 'usd' else item.price /
#
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     intent = stripe.PaymentIntent.create(
#         amount=item.price,
#         currency='usd',
#     )
#
#     return JsonResponse({'payment_intent_id': intent.client_secret})

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
