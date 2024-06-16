from django.contrib import admin
from .models import Category, FoodItem

class FoodItemInline(admin.TabularInline):
    model = FoodItem
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [FoodItemInline]

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(FoodItem, FoodItemAdmin)
