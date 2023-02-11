from django.urls import path
from payments.views import (
    create_checkout_session,
    PaymentFailedView,
    PaymentSuccessView
)

app_name = 'payments'

urlpatterns = [
    path(
        'buy/<int:pk>/',
        create_checkout_session,
        name='create_checkout_session'
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
