from django.shortcuts import render, redirect, get_object_or_404
from django.views import *

from shop.models import Product
from shop.utils import *
from .cart import Cart
from .forms import CartAddProductForm


class CartAdd(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        form = CartAddProductForm(self.request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})
