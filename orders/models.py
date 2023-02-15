from django.db import models

from items.models import Item


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return int(sum(item.get_cost() for item in self.items.all()))


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Item,
        related_name='order_items',
        on_delete=models.CASCADE
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена товара'  # Цена в центах
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
