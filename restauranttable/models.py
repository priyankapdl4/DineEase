# reservations/models.py
from django.db import models
from django.conf import settings

class Table(models.Model):
    number = models.IntegerField(unique=True)
    seats = models.IntegerField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.number}"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()  
    time = models.TimeField()
    reservation_time = models.DateTimeField()

    def __str__(self):
        return f'Reservation for {self.name} at {self.table}'

   
