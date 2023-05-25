from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from courses.models import Courses
import stripe


class SuccessPayment(TemplateView):
    template_name = 'success.html'


class CancelPayment(TemplateView):
    template_name = 'cancel.html'


class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        stripe.api_key = settings.STRIPE_SECRET_KEY
        course = Courses.objects.get(pk=self.kwargs['pk'])
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': course.price,
                    'product_data': {
                        'name': course.title,
                        },
                    },
                'quantity': 1,
                },
            ],
            metadata={
                "course_id": course.id
            },
            mode='payment',
            success_url='http://127.0.0.1:8000/course/payment/success/',
            cancel_url='http://127.0.0.1:8000/course/payment/cancel/',
            )

        return redirect(checkout_session.url, code=303)
