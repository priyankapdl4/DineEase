from django import forms
from .models import Table, Reservation
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime  # Import datetime module

class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ['number', 'seats', 'is_booked']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'seats': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_booked': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['table', 'name', 'email', 'date', 'time']
        widgets = {
            'table': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < timezone.now().date():
            raise ValidationError("The reservation date cannot be in the past.")
        return date

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # Ensure date and time are not in the past
        if date and time:
            now = timezone.now()
            reservation_datetime = timezone.make_aware(datetime.datetime.combine(date, time))
            if reservation_datetime < now:
                raise ValidationError("The reservation time cannot be in the past.")

        return cleaned_data
