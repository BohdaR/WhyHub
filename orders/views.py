from django.shortcuts import render, redirect

from shop.models import Product
from .models import OrderItem
from .forms import OrderCreateForm
from django.views.generic import FormView
from cart.cart import Cart


class OrderCreate(FormView):
    template_name = 'orders/create.html'
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)
        errors = 'Недостатньо на складі: '
        for item in cart:
            if item['quantity'] > item['product'].stock:
                errors += f"{item['product']} залишилось - {item['product'].stock}\n"

        if errors != 'Недостатньо на складі: ':
            return self.render_to_response(self.get_context_data(form=form, errors=errors))

        order = form.save()
        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])

            product = Product.objects.get(id=item['product'].id)
            product.stock = item['product'].stock - item['quantity']

            if item['product'].stock - item['quantity'] == 0:
                product.available = False
            product.save()

        cart.clear()
        return render(self.request, 'orders/created.html',
                      {'order': order})

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))
