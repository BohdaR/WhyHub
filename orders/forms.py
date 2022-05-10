from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'city', 'address', 'phone_number', 'delivery_method', 'pay_method']
        widgets = {
            'first_name':forms.TextInput(attrs={
                'placeholder': 'Ім\'я'}),
            'last_name':forms.TextInput(attrs={
                'placeholder': 'Прізвище'}),
            'email':forms.TextInput(attrs={
                'placeholder': 'Eмейл'}),
            'address':forms.TextInput(attrs={
                'placeholder': 'Адреса доставки'}),
            'phone_number':forms.TextInput(attrs={
                'placeholder': 'Номер телефону'}),
            'city':forms.TextInput(attrs={
                'placeholder': 'Ваше місто'}),
            'delivery_method': forms.RadioSelect(attrs={
                'class': 'order-chekbox'}),
            'pay_method': forms.RadioSelect(attrs={
                'class': 'order-chekbox'}),
        }