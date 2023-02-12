from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название товара'
    )
    description = models.TextField(
        verbose_name='Описание товара'
    )
    price = models.IntegerField(
        default=0,
        verbose_name='Цена товара'  # Цена в центах
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)
