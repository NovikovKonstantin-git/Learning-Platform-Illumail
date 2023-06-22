from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
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
                    'currency': 'byn',
                    'unit_amount': course.price*100,
                    'product_data': {
                        'name': course.title,
                        'description': f"{course.about_the_course} Автор курса: {str(course.author)} ({str(course.author.last_name)} {str(course.author.first_name)} {str(course.author.patronymic)})",
                        },
                    },
                'quantity': 1,
                },
            ],
            phone_number_collection={
                'enabled': True,
            },
            metadata={
                "course_id": course.id
            },
            mode='payment',
            success_url=f'http://127.0.0.1:8000/course/payment/success/',
            cancel_url=f'http://127.0.0.1:8000/course/payment/cancel/',
            )

        return redirect(checkout_session.url, code=303)


# @method_decorator(csrf_exempt, name="dispatch")
# class StripeWebhookView(View):
#     def get(self, request, format=None):
#         payload = request.body
#         endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
#         sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
#         event = None
#
#         try:
#             event = stripe.Webhook.construct_event(payload, sig_header, endpoint_secret)
#             print('allls')
#         except ValueError as e:
#             return HttpResponse('invalid 1')
#         except stripe.error.SignatureVerificationError as e:
#             return HttpResponse('invalid 2')
#
#         if event["type"] == "checkout.session.completed":
#             print("Payment successful")
#
#             # Add this
#             session = event["data"]["object"]
#             course = session["metadata"]["course_id"]
#
#         return HttpResponse(status=200)
@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    print(payload)
    return HttpResponse(status=200)