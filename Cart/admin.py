from django.contrib import admin
from .models import Carts,CartItem

# Register your models here.

@admin.register(Carts)
class CartsAdmin(admin.ModelAdmin):
    list_display = ['id','cart_id','date_added']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id','product','cart','quantity','is_active']