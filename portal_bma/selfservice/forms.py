from django import forms
from django.utils.translation import ugettext_lazy as _

import requests

from selfservice.constants import DAYS, EVENT_TYPE, COSTUME
from selfservice.models import AnchorBooking
from datetime import datetime


class CheckAvailableForm(forms.Form):
    function_date = forms.CharField(
        label=_("Date"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border', 'id': 'datepicker'})
    )
    function_start = forms.CharField(
        label=_("Start Time"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border input-small', 'id': 'timepicker1'})
    )
    function_end = forms.CharField(
        label=_("End Time"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border input-small', 'id': 'timepicker2'})
    )
    function_days = forms.ChoiceField(
        label=_("Days"),
        choices=DAYS,
        initial=DAYS,
        widget=forms.Select({'class': 'form-control input_border'})
    )
    function_state = forms.CharField(
        label=_("State"),
        max_length=30,
        widget=forms.Select({'class': 'form-control input_border', 'id': 'listBox',
                             'onchange': 'selct_district(this.value)'})
    )
    function_place = forms.CharField(
        label=_("District"),
        max_length=30,
        widget=forms.Select({'class': 'form-control input_border', 'id': 'secondlist'})
    )

    def clean_function_end(self):
        function_start = self.cleaned_data.get("function_start")
        function_end = self.cleaned_data.get("function_end")
        function_date = self.cleaned_data.get("function_date")
        start = function_date + " " + function_start
        end = function_date + " " + function_end
        datetime_object_start = datetime.strptime(start, '%m/%d/%Y %I:%M %p')
        datetime_object_end = datetime.strptime(end, '%m/%d/%Y %I:%M %p')
        time_difference = datetime_object_end - datetime_object_start
        if time_difference.days < 0 :
            raise forms.ValidationError("Something wrong in date or time")
        else:
            return function_start


class BookingCustomerForm(forms.Form):
    first_name = forms.CharField(
        label=_("First Name"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border'})
    )
    last_name = forms.CharField(
        label=_("Last Name"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border'})
    )
    customer_email = forms.EmailField(
        label=_("Email ID"),
        max_length=30,
        widget=forms.EmailInput({'class': 'form-control input_border'})
    )
    company_name = forms.CharField(
        label=_("Company Name"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border'})
    )
    mobile_number = forms.CharField(
        label=_("Mobile Number"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border'})
    )
    phone_number = forms.CharField(
        label=_("Phone Number"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border'})
    )
    address = forms.CharField(
        label=_("Address"),
        max_length=500,
        widget=forms.Textarea({'class': 'form-control input_border', 'rows': 3})
    )


class BookingEventForm(forms.Form):
    event_type = forms.ChoiceField(
        label=_("Event Type"),
        choices=EVENT_TYPE,
        widget=forms.Select({'class': 'form-control input_border'})
    )
    event_place = forms.CharField(
        label=_("Event Place"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border'})
    )
    event_venue = forms.CharField(
        label=_("Event Venue"),
        max_length=30,
        widget=forms.TextInput({'class': 'form-control input_border'})
    )
    costume = forms.ChoiceField(
        label=_("Costume"),
        choices=COSTUME,
        widget=forms.Select({'class': 'form-control input_border'})
    )
    about_event = forms.CharField(
        label=_("Event Briefing"),
        max_length=1000,
        widget=forms.Textarea({'class': 'form-control input_border', 'rows': 3})
    )