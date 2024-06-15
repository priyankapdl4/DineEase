# reservations/urls.py
from django.urls import path
from .views import table_list, reserve_table

urlpatterns = [
    path('', table_list, name='table_list'),
    path('reserve/<int:table_id>/', reserve_table, name='reserve_table'),
]
