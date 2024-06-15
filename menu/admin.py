from django.contrib import admin
from django.utils.html import format_html
from .models import FoodItem, Order

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'image_tag')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.image.url))
        return "No Image"
    image_tag.short_description = 'Image'

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)
    filter_horizontal = ('food_items',)

admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Order, OrderAdmin)
