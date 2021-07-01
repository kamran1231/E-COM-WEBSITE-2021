from django.shortcuts import render,redirect
from Store.models import Product
from .models import Carts,CartItem
# Create your views here.


#this will give session id
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request,product_id):
    product = Product.objects.get(id=product_id) #get the product
    try:
        #get the cart using cart_id present in the session
        cart = Carts.objects.get(cart_id=_cart_id(request))
    except Carts.DoesNotExist:
        cart = Carts.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,cart=cart,quantity=1
        )

        cart_item.save()
    return redirect('cart')


def remove_cart(request,product_id):
    product = Product.objects.get(id=product_id)
    cart = Carts.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    product = Product.objects.get(id=product_id)
    cart = Carts.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(cart=cart,product=product)

    cart_item.delete()
    return redirect('cart')


def cart(request,total=0,quantity=0,cart_items=None):
    try:
        cart = Carts.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

    except:
        pass
    tax = (8 * total) / 100
    discount = (2 * total)/100
    grand_total = (total + tax - discount)

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'grand_total':grand_total,
        'tax':tax,
        'discount':discount
    }

    return render(request,'cart/cart.html',context)