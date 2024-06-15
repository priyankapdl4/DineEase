# menu/views.py
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .models import FoodItem, Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def menu_view(request):
    food_items = FoodItem.objects.all()
    return render(request, 'menu/menu.html', {'food_items': food_items})

def add_to_order(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.get(id=order_id)
    else:
        order = Order.objects.create()
        request.session['order_id'] = order.id
    order.food_items.add(food_item)
    return redirect('menu')

def delete_from_order(request, food_id):
    food_item = get_object_or_404(FoodItem, id=food_id)
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.get(id=order_id)
        order.food_items.remove(food_item)
    return redirect('view_order')

def view_order(request):
    order_id = request.session.get('order_id')
    if order_id:
        order = Order.objects.get(id=order_id)
    else:
        order = None
    return render(request, 'menu/order.html', {'order': order})

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect ('menu')
        else:
            return HttpResponse("Username or password is incorret!!")
        
    return render(request, 'menu/login.html')

def signupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')

        if password1!=password2:
            return HttpResponse("Your password and confirm password is not same!!" )
        my_user=User.objects.create_user(username,email,password1)
        my_user.save()
        return redirect('login_page')

        

    return render(request, 'menu/signupp.html')
