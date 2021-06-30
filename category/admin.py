from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','slug','description','cat_image']
    #automatic slug create
    prepopulated_fields = {'slug':['category_name']}

