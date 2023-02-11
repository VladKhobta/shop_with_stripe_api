import stripe
from stripe.api_resources.apps import Secret


def create_payment_intent(
        amount: int,
        currency: str,
) -> (str, Secret):

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
    )

    return intent.id, intent.client_secret
