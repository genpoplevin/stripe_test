import os
from dotenv import load_dotenv
from django.views.generic import DetailView

from items.models import Item

load_dotenv()


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = os.getenv('STRIPE_PUBLISHABLE_KEY')
        return context
