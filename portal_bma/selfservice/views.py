import requests
from django.shortcuts import render_to_response, HttpResponseRedirect, redirect
from django.template.context import RequestContext
from django.contrib.auth.models import User
from selfservice.models import UserProfile, AnchorVideo, AnchorBooking, AnchorLanguage
from selfservice.forms import CheckAvailableForm, BookingCustomerForm, BookingEventForm
from django.conf import settings
import os
from django.contrib import messages
from django.db import IntegrityError, transaction
from datetime import datetime
from uuid import uuid4
from django.contrib.auth import logout
import razorpay
from selfservice.razorpay import *

# Create your views here.


def home(request):
    return render_to_response(
        'selfservice/index.html', locals(), context_instance=RequestContext(request)
    )


def landing_page(request):
    anchors = UserProfile.objects.filter(is_anchor=True)
    celebrity_anchor = UserProfile.objects.filter(is_celebrity=True)
    return render_to_response(
        'selfservice/landingpage.html', locals(), context_instance=RequestContext(request)
    )


@transaction.atomic
def view_profile(request, anchor_id):
    if request.method == 'POST':
        check_available_form = CheckAvailableForm(request.POST)
        if check_available_form.is_valid():
            function_date = check_available_form.cleaned_data.get("function_date", "")
            user_profile = UserProfile.objects.get(id=anchor_id)
            try:
                is_available = AnchorBooking.objects.get(user=user_profile.user, booking_date=function_date)
                messages.error(request, "Anchor Busy for this day")
            except AnchorBooking.DoesNotExist:
                function_start = check_available_form.cleaned_data.get("function_start", "")
                function_end = check_available_form.cleaned_data.get("function_end", "")
                function_days = check_available_form.cleaned_data.get("function_days", "")
                function_state = check_available_form.cleaned_data.get("function_state", "")
                function_place = check_available_form.cleaned_data.get("function_place", "")

                duration = calculate_duration(function_date, function_start, function_end)

                amount = fix_budget(function_start, function_end, function_days, function_state,
                                    function_place, duration, user_profile)
                message = "Anchor Available for this days program. Total amount will be %s" % amount
                messages.success(request, message)

                anchor_booking = AnchorBooking()
                anchor_booking.booking_user = request.user
                anchor_booking.user = user_profile.user
                anchor_booking.unique_id = uuid4()
                anchor_booking.function_start = function_start
                anchor_booking.function_end = function_end
                anchor_booking.function_date = function_date
                anchor_booking.function_days = function_days
                anchor_booking.function_place = function_place
                anchor_booking.function_state = function_state
                anchor_booking.booking_date = datetime.now().strftime('%m/%d/%Y')
                anchor_booking.total = amount
                anchor_booking.save()
    else:
        check_available_form = CheckAvailableForm()
    user_profile = UserProfile.objects.get(id=anchor_id)
    user_languages = AnchorLanguage.objects.filter(user__username=user_profile.user.username)
    user_username = user_profile.user.username
    file_path = settings.STATIC_ROOT + user_profile.image_path
    count = 0
    for f in os.listdir(file_path):
        if os.path.isfile(os.path.join(file_path, f)):
            count += 1
    image_count = list()
    image_count = range(1, count)
    anchor_video = AnchorVideo.objects.filter(user__username=user_username)
    return render_to_response(
        'selfservice/viewprofile.html', locals(), context_instance=RequestContext(request)
    )


def fix_budget(function_start, function_end, function_days, function_state, function_place, duration, user_profile):
    amount = int(user_profile.charge)
    if duration > 5:
        duration_difference = duration - 5
        for time in range(0, duration_difference):
            amount += 500
    if int(function_days) > 3:
        days_difference = int(function_days) - 3
        for days in range(0, days_difference):
            amount -= 1500
    return amount


def calculate_duration(function_date, function_start, function_end):
    start = function_date + " " + function_start
    end = function_date + " " + function_end
    datetime_object_start = datetime.strptime(start, '%m/%d/%Y %I:%M %p')
    datetime_object_end = datetime.strptime(end, '%m/%d/%Y %I:%M %p')
    time_difference = (datetime_object_end - datetime_object_start).seconds
    minutes = time_difference / 60
    hour = minutes / 60
    return hour


def booking(request, booking_id, anchor_id):

    try:
        anchor_booking = AnchorBooking.objects.get(id=booking_id)
        user_profile = UserProfile.objects.get(id=anchor_id)
        
    except AnchorBooking.DoesNotExist:
        pass

    if request.method == "POST":
        customer_form = BookingCustomerForm(request.POST)
        if customer_form.is_valid():
            first_name = customer_form.cleaned_data.get("first_name")
            last_name = customer_form.cleaned_data.get("last_name")
            customer_email = customer_form.cleaned_data.get("customer_email")
            company_name = customer_form.cleaned_data.get("company_name")
            address = customer_form.cleaned_data.get("address")
            mobile_number = customer_form.cleaned_data.get("mobile_number")
            phone_number = customer_form.cleaned_data.get("phone_number")
            anchor_booking.first_name = first_name
            anchor_booking.last_name = last_name
            anchor_booking.customer_email_id = customer_email
            anchor_booking.company_name = company_name
            anchor_booking.mobile_number = mobile_number
            anchor_booking.phone_number = phone_number
            anchor_booking.address = address
            anchor_booking.save()
            event_form = BookingEventForm()
    else:
        customer_form = BookingCustomerForm()

    return render_to_response(
        'selfservice/customer_data.html', locals(), context_instance=RequestContext(request)
    )


def event_booking(request, booking_id, anchor_id):
    try:
        anchor_booking = AnchorBooking.objects.get(id=booking_id)
        user_profile = UserProfile.objects.get(id=anchor_id)

    except AnchorBooking.DoesNotExist:
        pass
    if request.method == "POST":
        event_form = BookingEventForm(request.POST)
        if event_form.is_valid():
            event_type = event_form.cleaned_data.get("event_type")
            event_place = event_form.cleaned_data.get("event_place")
            event_venue = event_form.cleaned_data.get("event_venue")
            costume = event_form.cleaned_data.get("costume")
            about_event = event_form.cleaned_data.get("about_event")
            anchor_booking.event_type = event_type
            anchor_booking.event_place = event_place
            anchor_booking.event_venue = event_venue
            anchor_booking.costume = costume
            anchor_booking.about_event = about_event
            anchor_booking.save()
            payment = True
            return render_to_response(
                'selfservice/payment.html', locals(), context_instance=RequestContext(request)
            )
    else:
        payment = False
    return render_to_response(
        'selfservice/customer_data.html', locals(), context_instance=RequestContext(request)
    )


def booking_completed(request, razorpay_id, booking_id):
    try:
        anchor_booking = AnchorBooking.objects.get(id=booking_id)
        anchor_booking.razorpay_id = razorpay_id
        anchor_booking.save()
        send_invoice(request, booking_id)
    except AnchorBooking.DoesNotExist:
        pass


def logout_view(request):
    logout(request)
    return redirect('/')