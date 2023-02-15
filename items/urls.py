from django.urls import path
from items.views import ItemDetailView, ItemListView

app_name = 'items'

urlpatterns = [
    path(
        '',
        ItemListView.as_view(),
        name='item_list'
    ),
    path(
        'item/<int:pk>/',
        ItemDetailView.as_view(),
        name='item_detail'
    ),
]
