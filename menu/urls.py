from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),
    path('add/<int:food_id>/', views.add_to_order, name='add_to_order'),
    path('order/', views.view_order, name='view_order'),
    path('delete/<int:food_id>/', views.delete_from_order, name='delete_from_order'),
    path('login/', views.loginPage, name='login_page'),
    path('signup/', views.signupPage, name='signup_page'),
]
