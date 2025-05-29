from django.forms import ModelForm
from django import forms
from .models import Product, Shop, Cost

class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['nume_produs'].widget.attrs.update({'class': 'input'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})
    class Meta:
        model = Product
        fields = ['nume_produs', 'product_image', 'nume_magazin', 'descriere', 'producator', 'calorii', 'pret']
        widgets = {
            'nume_magazin': forms.CheckboxSelectMultiple(),
        }

class ShopForm(ModelForm):
    class Meta:
        model  = Shop
        fields = '__all__'

class CostForm(ModelForm):
    class Meta:
        model  = Cost
        fields = '__all__'