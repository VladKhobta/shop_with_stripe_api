from rest_framework import serializers

from .models import Payment
from .service import create_payment_intent


class PaymentSerializer(serializers.ModelSerializer):
    client_secret = serializers.SerializerMethodField()  # method's name is the get_(client_secret) by default

    class Meta:
        model = Payment
        fields = '__all__'

    def get_client_secret(self, payment: Payment) -> str:
        return payment._client_secret if hasattr(payment, "_client_secret") else None

    def create(self, validated_data: dict) -> Payment:
        instance = super().create(validated_data)

        stripe_id, client_id = create_payment_intent(
            amount=instance.amount,
            currency=instance.currency,
        )

        instance.stripe_id = stripe_id,
        instance._client_secret = client_id
        instance.save()

        return instance
