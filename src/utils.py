import stripe

stripe.api_key = 'your-stripe-secret-key'

def process_payment(amount, token):
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Convert dollars to cents
            currency='usd',
            description='Charge for product purchase',
            source=token
        )
        return charge
    except stripe.error.StripeError as e:
        return {'error': str(e)}