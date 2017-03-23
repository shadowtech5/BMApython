"""portal_bma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from selfservice.views import home, landing_page, view_profile, booking, event_booking, booking_completed, logout_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, {}, "home"),
    url(r'^landing_page/', landing_page, {}, "landingpage"),
    url(r'^view_profile/(?P<anchor_id>\d+)/$', view_profile, name='viewprofile'),
    url(r'^(?P<booking_id>\d+)/booking/(?P<anchor_id>\d+)/$', booking, name='Booking'),
    url(r'^(?P<booking_id>\d+)/event_booking/(?P<anchor_id>\d+)/$', event_booking, name='Event_Booking'),
    url(r'^booking_completed/(?P<razorpay_id>.*)/(?P<booking_id>\d+)/$', booking_completed, name="booking_completed"),
    url('', include('social_django.urls', namespace='auth')),
    url(r'^logout/$', logout_view, {}, "logout"),
]
