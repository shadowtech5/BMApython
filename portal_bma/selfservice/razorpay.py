import razorpay
from selfservice.models import *
from django.conf import settings


def connect_razorpay():

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY, settings.RAZORPAY_SECRET))
    return client


def send_invoice(request, booking_id):
    try:
        anchor_booking = AnchorBooking.objects.get(id=booking_id)
        client = connect_razorpay()
        DATA = {
            "customer": {
                "email": anchor_booking.customer_email_id,
                "contact": anchor_booking.mobile_number,
                "name": anchor_booking.first_name + anchor_booking.last_name
            },
            "amount": anchor_booking.amount,
            "currency": "INR",
            "sms_notify": "0",
            "email_notify": "1"
        }
        client.invoice.create(data=DATA)
    except AnchorBooking.DoesNotExist:
        pass
