from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Client, ClientType, Product, Order

class ClientTypeForm(forms.ModelForm):
    class Meta:
        model = ClientType
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
class ProductForm(forms.Form):
    PRODUCT_CATEGORIES = [
        ('Food', 'Food'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
        ('Hardware', 'Hardware'),
    ]

    product_name = forms.CharField(max_length=100)
    category = forms.ChoiceField(choices=PRODUCT_CATEGORIES)
    description = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField(min_value=1, max_value=5)