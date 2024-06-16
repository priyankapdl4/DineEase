from django.shortcuts import render
from .models import Category, FoodItem

def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})
