import os

from django.views.generic import DetailView, ListView
from dotenv import load_dotenv

from cart.forms import CartAddItemForm
from items.models import Item

load_dotenv()


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = os.getenv('STRIPE_PUBLISHABLE_KEY')
        context['cart_item_form'] = CartAddItemForm()
        return context


class ItemListView(ListView):
    model = Item
    template_name = 'item/item_list.html'
