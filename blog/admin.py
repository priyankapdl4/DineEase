from django.contrib import admin
from .models import Event, Offer

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')
    list_filter = ('date',)

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'discount_percentage')
    search_fields = ('title', 'description')
    list_filter = ('discount_percentage',)

admin.site.register(Event, EventAdmin)
admin.site.register(Offer, OfferAdmin)
