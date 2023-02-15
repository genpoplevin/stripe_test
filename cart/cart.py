from decimal import Decimal

from django.conf import settings

from items.models import Item


class Cart(object):

    def __init__(self, request):
        """Инициализация объекта корзины."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем в сессии пустую корзину.
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, item, quantity=1, update_quantity=False):
        """Добавление товара в корзину или обновление его количества."""
        item_id = str(item.id)
        if item_id not in self.cart:
            self.cart[item_id] = {
                'quantity': 0,
                'price': str(item.price)
            }
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def save(self):
        """Помечаем сессию как изменённую."""
        self.session.modified = True

    def remove(self, item):
        """Удаление товара из корзины."""
        item_id = str(item.id)
        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def __iter__(self):
        """
        Проходим по товарам корзины и получаем соотвествующие объекты Item.
        """
        item_ids = self.cart.keys()
        # Получаем объекты модели Item и передаём их в корзину.
        items = Item.objects.filter(id__in=item_ids)

        cart = self.cart.copy()
        for item in items:
            cart[str(item.id)]['item'] = item
        for element in cart.values():
            element['price'] = Decimal(element['price'])
            element['total_price'] = (
                element['price']
                * element['quantity']
                / 100
            )
            yield element

    def __len__(self):
        """Возвращает общее количество товаров в корзине."""
        return sum(element['quantity'] for element in self.cart.values())

    def get_total_price(self):
        """Считает общую стоимость корзины."""
        return sum(
            Decimal(element['price']) * element['quantity'] / 100
            for element in self.cart.values()
        )

    def clear(self):
        """Очистка корзины."""
        del self.session[settings.CART_SESSION_ID]
        self.save()
