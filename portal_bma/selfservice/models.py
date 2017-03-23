from __future__ import unicode_literals
from django.contrib.auth.models import User

from selfservice.constants import STATE, EVENT_TYPE, COSTUME, ANCHOR_TYPE

from django.db import models

# Create your models here.

GENDER = (
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE')
)

STAR_RATING = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5')
)

LANGUAGE = (
    ('ENGLISH', 'ENGLISH'),
    ('MALAYALAM', 'MALAYALAM'),
    ('TAMIL', 'TAMIL'),
    ('KANNADA', 'KANNADA'),
    ('PUNJABI', 'PUNJABI'),
    ('TELUGU', 'TELUGU'),
    ('MARATHI', 'MARATHI'),
    ('HINDI', 'HINDI'),
    ('ARABIC', 'ARABIC'),
    ('FRENCH', 'FRENCH'),
)

EVENT_TYPE = (
    ('SHOW', 'SHOW'),
    ('CAMPUS', 'CAMPUS'),
    ('KIDS PARTY', 'KIDS PARTY'),
    ('PRIVATE PARTY', 'PRIVATE PARTY'),
    ('INAUGURATION', 'INAUGURATION'),
    ('CORPRATE', 'CORPRATE'),
    ('PROMOTIONS', 'PROMOTIONS'),
    ('EXIBITIONS', 'EXIBITIONS'),
    ('FASHION SHOW', 'FASHION SHOW'),
    ('WEDDING', 'WEDDING')
)

AVAILABLE_OPTION = (
    ('ONLINE', 'ONLINE'),
    ('OFFLINE', 'OFFLINE'),
    ('BUSY', 'BUSY')
)

TRAVEL = (
    ('KERALA', 'KERALA'),
    ('NATIONAL', 'NATIONAL'),
    ('INTERNATIONAL', 'INTERNATIONAL')
)


class AchorType(models.Model):
    user = models.ForeignKey(User)
    anchor_type = models.CharField(max_length=50, choices=ANCHOR_TYPE)


class EventTypes(models.Model):
    user = models.ForeignKey(User)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_celebrity = models.BooleanField(default=False)
    is_anchor = models.BooleanField(default=False)
    bma_code = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    place = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)
    biography = models.reason = models.TextField(null=True)
    star_rating = models.CharField(max_length=10, choices=STAR_RATING, blank=True, null=True)
    charge = models.CharField(max_length=10, blank=True, null=True)
    preffered_place = models.CharField(max_length=50, choices=TRAVEL, blank=True, null=True)
    image_path = models.CharField(max_length=100, blank=True, null=True)
    type = models.ManyToManyField(AchorType, blank=True)
    event_preffered = models.ManyToManyField(EventTypes, blank=True)


class AnchorLanguage(models.Model):
    user = models.ForeignKey(User)
    language = models.CharField(max_length=50, choices=LANGUAGE)


class AnchorActive(models.Model):
    user = models.ForeignKey(User)
    date = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    available = models.CharField(max_length=50, choices=AVAILABLE_OPTION)


class AnchorTravel(models.Model):
    user = models.ForeignKey(User)
    travel = models.CharField(max_length=50, choices=TRAVEL)


class AnchorVideo(models.Model):
    user = models.ForeignKey(User)
    video_id = models.CharField(max_length=50, blank=True, null=True)


class AnchorStatePrice(models.Model):
    state = models.CharField(max_length=50, choices=STATE)
    place = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)


class AnchorBooking(models.Model):
    user = models.ForeignKey(User)
    booking_user = models.CharField(max_length=50, blank=True, null=True)
    unique_id = models.CharField(max_length=50, blank=True, null=True)
    booking_date = models.CharField(max_length=50, blank=True, null=True)
    function_date = models.CharField(max_length=50, blank=True, null=True)
    function_start = models.CharField(max_length=50, blank=True, null=True)
    function_end = models.CharField(max_length=50, blank=True, null=True)
    function_days = models.CharField(max_length=50, blank=True, null=True)
    function_state = models.CharField(max_length=50, blank=True, null=True)
    function_place = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    customer_email_id = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE)
    event_place = models.CharField(max_length=50, blank=True, null=True)
    event_venue = models.CharField(max_length=50, blank=True, null=True)
    costume = models.CharField(max_length=50, choices=COSTUME)
    about_event = models.TextField()
    total = models.CharField(max_length=50, blank=True, null=True)
    razorpay_id = models.CharField(max_length=50, blank=True, null=True)





