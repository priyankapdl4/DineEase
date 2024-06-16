from django.shortcuts import render, get_object_or_404
from .models import Category, FoodItem

def menu(request):
    categories = Category.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})


