from django.shortcuts import render, get_object_or_404
# import Cart class from cart.py
from .cart import Cart
from Store.models import Product

# json response
from django.http import JsonResponse

# Create your views here.
def cart_summary(request):
    return render(request, "cart_summary.html")

def cart_add(request):
    # get the cart
    cart = Cart(request)
    # test for Post
    if request.POST.get('action') == 'post':
    # get stuff
        product_id = int(request.POST.get('product_id'))
        # look up product in db
        product = Product.objects.get(id=product_id)
        # save to a session
        cart.add(product=product)

        # Get cart Quantity
        cart_quantity = cart.__len__()

        # return response
        # response = JsonResponse({'Product Name: ': product.name})

        response = JsonResponse({'qty: ': cart_quantity})

        return  response



def cart_delete(request):
    return render(request, "cart_delete.html")

def cart_update(request):
    return render(request, "cart_update.html")