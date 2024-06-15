from django.shortcuts import render
from .models import Event, Offer

def index(request):
    events = Event.objects.all()
    offers = Offer.objects.all()
    return render(request, 'blog/index.html', {'events': events, 'offers': offers})
