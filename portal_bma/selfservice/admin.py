from django.contrib import admin

# Register your models here.

from selfservice.models import *


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bma_code')
    search_fields = ['user', 'bma_code']
    list_filter = ['gender']

admin.site.register(UserProfile, UserProfileAdmin)


class AnchorLanguageAdmin(admin.ModelAdmin):
    list_display = ('user', 'language')
    search_fields = ['user']
    list_filter = ['language']

admin.site.register(AnchorLanguage, AnchorLanguageAdmin)


class EventTypesAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type')
    search_fields = ['user']
    list_filter = ['event_type']

admin.site.register(EventTypes, EventTypesAdmin)


class AnchorActiveAdmin(admin.ModelAdmin):
    list_display = ('user', 'available', 'date', 'time')
    search_fields = ['user']
    list_filter = ['available']

admin.site.register(AnchorActive, AnchorActiveAdmin)


class AnchorTravelAdmin(admin.ModelAdmin):
    list_display = ('user', 'travel')
    search_fields = ['user']
    list_filter = ['travel']

admin.site.register(AnchorTravel, AnchorTravelAdmin)


class AnchorVideoAdmin(admin.ModelAdmin):
    list_display = ('user', 'video_id')
    search_fields = ['user', 'video_id']

admin.site.register(AnchorVideo, AnchorVideoAdmin)


class AnchorStatePriceAdmin(admin.ModelAdmin):
    list_display = ('state', 'place', 'price')
    search_fields = ['state', 'place']
    list_filter = ['state']

admin.site.register(AnchorStatePrice, AnchorStatePriceAdmin)


class AnchorBookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'booking_user', 'booking_date')
    search_fields = ['user', 'booking_user',]

admin.site.register(AnchorBooking, AnchorBookingAdmin)


class AnchorTypeAdmin(admin.ModelAdmin):
    list_display = ('user', 'anchor_type')

admin.site.register(AchorType, AnchorTypeAdmin)

