from django.contrib import admin

from items.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'price',
    )


admin.site.register(Item, ItemAdmin)
