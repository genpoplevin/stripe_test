import os

import stripe
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from dotenv import load_dotenv

from items.models import Item
from orders.models import Order

load_dotenv()


@require_http_methods(["GET"])
@csrf_exempt
def create_checkout_session_one_item(request, pk):

    item = get_object_or_404(Item, pk=pk)

    stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name
                    },
                    'unit_amount': item.price
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'sessionId': checkout_session.id})


@require_http_methods(["GET"])
@csrf_exempt
def create_checkout_session_order(request, pk):

    item = get_object_or_404(Order, pk=pk)

    stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': f'Pay for order {item.id}'
                    },
                    'unit_amount': item.get_total_cost()
                },
                'quantity': 1,
            }
        ],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'sessionId': checkout_session.id})


class PaymentSuccessView(TemplateView):
    template_name = 'payments/success.html'


class PaymentFailedView(TemplateView):
    template_name = 'payments/cancel.html'
