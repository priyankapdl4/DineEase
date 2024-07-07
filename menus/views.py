from django.shortcuts import render, get_object_or_404
from .models import Category, FoodItem
from order.models import Cart

def menu(request):
    categories = Category.objects.all()
    food = FoodItem.objects.all()
    name_quantity_of_all_food = []
    if(request.user.is_authenticated):
        cartitems = Cart.objects.filter(username=request.user)
        for f in food:
            find = False
            name_quantity_combo = []
            for item in cartitems:
                if(f.name == item.food.name):
                    name_quantity_combo.append(f.name)
                    name_quantity_combo.append(item.quantity)
                    find = True
                    break
            if(not find):
                name_quantity_combo.append(f.name)
                name_quantity_combo.append('0')
            name_quantity_of_all_food.append(name_quantity_combo)
    return render(request, 'menu/menu.html', {'categories': categories,'cartitems':name_quantity_of_all_food})


