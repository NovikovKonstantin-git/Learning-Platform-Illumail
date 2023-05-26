from django.urls import path
from payments.views import *

urlpatterns = [
    path('course/<int:pk>/payment/', CreateCheckoutSessionView.as_view(), name='payment'),
    path('course/payment/success/', SuccessPayment.as_view(), name='success_payment'),
    path('course/payment/cancel/', CancelPayment.as_view(), name='cancel_payment'),
    path('webhook/stripe/', StripeWebhookView.as_view(), name='stripe-webhook'),
]