from django import forms

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