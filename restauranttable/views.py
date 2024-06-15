# reservations/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import Table, Reservation
from .forms import ReservationForm
from django.utils import timezone

def table_list(request):
    tables = Table.objects.all()
    return render(request, 'reservations/table_list.html', {'tables': tables})

def reserve_table(request, table_id):
    table = Table.objects.get(id=table_id)
    if table.is_booked:
        return JsonResponse({'message': 'This table is already booked.'}, status=400)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table = table
            reservation.reservation_time = timezone.now()
            reservation.save()
            table.is_booked = True
            table.save()

        send_mail(
                'Table Reservation Confirmation',
                f'Your reservation for table {table.number} (Seats: {table.seats}) has been confirmed.',
                'dinease12@gmail.com',
                [reservation.email],
                fail_silently=False,
            )
        
        
        return JsonResponse({'message': 'Table has been successfully booked.'})
    else:
        form = ReservationForm()
    return render(request, 'reservations/reserve_table.html', {'form': form, 'table': table})
