from django.shortcuts import redirect,render
from Store.models import Product
def home(request):
    product = Product.objects.all().filter(is_available=True)
    context = {
        'product':product
    }
    return render(request,'home.html',context)