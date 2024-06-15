from django.contrib import admin
from django.db import transaction
from .models import Table, Reservation
from .forms import TableForm, ReservationForm

class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'is_booked')
    list_filter = ('is_booked',)
    actions = ['mark_as_free']
    form = TableForm

    @transaction.atomic
    def mark_as_free(self, request, queryset):
        try:
            queryset.update(is_booked=False)
            self.message_user(request, "Selected tables have been marked as free.")
        except Exception as e:
            self.message_user(request, f"An error occurred: {e}", level='error')
    mark_as_free.short_description = "Mark selected tables as free"

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('table', 'name', 'email', 'date', 'time', 'reservation_time')
    list_filter = ('date', 'time')
    actions = ['cancel_reservation']
    form = ReservationForm

    @transaction.atomic
    def cancel_reservation(self, request, queryset):
        try:
            for reservation in queryset:
                reservation.table.is_booked = False
                reservation.table.save()
                reservation.delete()
            self.message_user(request, "Selected reservations have been canceled.")
        except Exception as e:
            self.message_user(request, f"An error occurred: {e}", level='error')
    cancel_reservation.short_description = "Cancel selected reservations"

admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
