from django.contrib import admin
from .models import Product,Variation

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','slug','category','price','stock',
                    'created_date','modified_date','is_available']
    list_display_links = ['id','product_name']

    prepopulated_fields = {'slug':['product_name']}

@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ['id','product','variation_category','variation_value',
                    'created_date','is_active']
    list_editable = ['is_active']
    list_filter = ['id','product','variation_category','variation_value',
                    'created_date']
    list_display_links = ['id','product']

