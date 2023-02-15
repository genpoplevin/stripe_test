import os

from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from dotenv import load_dotenv

from cart.cart import Cart
from cart.forms import CartAddItemForm
from items.models import Item

load_dotenv()


@require_POST
def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            item=item,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddItemForm(
            initial={'quantity': item['quantity'],
                     'update': True}
        )
    stripe_publishable_key = os.getenv('STRIPE_PUBLISHABLE_KEY')
    return render(
        request,
        'cart/detail.html',
        {
            'cart': cart,
            'stripe_publishable_key': stripe_publishable_key}
        )
