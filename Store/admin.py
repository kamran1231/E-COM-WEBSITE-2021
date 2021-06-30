from django.contrib import admin
from .models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','slug','category','price','stock',
                    'created_date','modified_date','is_available']
    list_display_links = ['id','product_name']

    prepopulated_fields = {'slug':['product_name']}

