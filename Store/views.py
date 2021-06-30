from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request,category_slug=None):
    categories = None
    product = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        product = Product.objects.filter(category=categories,is_available=True)
        product_count = product.count()
    else:
        product = Product.objects.all().filter(is_available=True)
        product_count = product.count()
    context = {
        'product':product,
        'product_count':product_count
    }
    return render(request,'store/store.html',context)

