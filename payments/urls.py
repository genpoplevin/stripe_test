from django.urls import path

from payments.views import (PaymentFailedView, PaymentSuccessView,
                            create_checkout_session_one_item,
                            create_checkout_session_order)

app_name = 'payments'

urlpatterns = [
    path(
        'buy/<int:pk>/',
        create_checkout_session_one_item,
        name='create_checkout_session_one_item'
    ),
    path(
        'buy/order/<int:pk>/',
        create_checkout_session_order,
        name='create_checkout_session_order'
    ),
    path(
        'success/',
        PaymentSuccessView.as_view(),
        name='success'
    ),
    path(
        'cancel/',
        PaymentFailedView.as_view(),
        name='cancel'
    ),
]
