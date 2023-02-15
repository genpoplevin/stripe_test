import os

from dotenv import load_dotenv
from django.shortcuts import render

from cart.cart import Cart
from orders.models import OrderItem
from orders.forms import OrderCreateForm


load_dotenv()


def order_create(request):
    cart = Cart(request)
    stripe_publishable_key = os.getenv('STRIPE_PUBLISHABLE_KEY')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for element in cart:
                OrderItem.objects.create(
                    order=order,
                    product=element['item'],
                    price=element['price'],
                    quantity=element['quantity']
                )
            # Очищаем корзину.
            cart.clear()
            return render(
                request,
                'orders/order/created.html',
                {'order': order, 'stripe_publishable_key': stripe_publishable_key}
            )
    else:
        form = OrderCreateForm()
    return render(
        request,
        'orders/order/create.html',
        {'cart': cart, 'form': form, 'stripe_publishable_key': stripe_publishable_key}
    )
