from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from django.views.generic import FormView
from cart.cart import Cart
from django.urls import reverse_lazy


class OrderCreate(FormView):
    template_name = 'orders/create.html'
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
        cart.clear()
        return render(self.request, 'orders/created.html',
                      {'order': order})

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))








# def order_create(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         form = OrderCreateForm(request.POST)
#         if form.is_valid():
#             order = form.save()
#             for item in cart:
#                 OrderItem.objects.create(order=order,
#                                          product=item['product'],
#                                          price=item['price'],
#                                          quantity=item['quantity'])
#             # очистка корзины
#             cart.clear()
#             return render(request, 'orders/created.html',
#                           {'order': order})
#     else:
#         form = OrderCreateForm
#     return render(request, 'orders/create.html',
#                   {'cart': cart, 'form': form})
