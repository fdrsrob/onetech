from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image', 'category']

class EditProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image', 'category']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            # Suponiendo que usas este campo para subir imágenes
        }

class DeleteProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = []