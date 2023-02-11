from django.conf import settings
from django.views.generic import DetailView

from items.models import Item


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        context['stripe_publishable_key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
