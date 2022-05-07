from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django.forms import ModelForm
from .models import Proveedor
from .models import Producto


class ProveedorForm(ModelForm):

    class Meta:
        model=Proveedor
        fields=['nombre', 'marca', 'telefono', 'correo_electronico']
    
    labels = {
        'nombre':  'Nombre de representante',
        'marca': 'Marca',
        'telefono': 'Teléfono de contacto',
        'correo_electronico': 'Email',
    }


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ProductoForm(ModelForm):
    
    CATEGORIA_CHOICES=( 

    ("H", "Hombre"), 

    ("M", "Mujer"), 

    ("U", "Unisex"),

    )

    COLOR_CHOICES=( 

    ("Blanco", "Blanco"), 

    ("Negro", "Negro"), 

    ("Gris", "Gris"),

    )

    TALLA_CHOICES=( 

    ("Small", "S"), 

    ("Medium", "M"), 

    ("Large", "L"),

    ("XLarge", "XL"),

    )

    class Meta:
        model=Producto
        fields=['nombre', 'categoria', 'marca', 'precio', 'stock', 'color', 'talla', 'imagen']

    color= forms.ChoiceField(choices=COLOR_CHOICES)

    talla= forms.ChoiceField(choices=TALLA_CHOICES)

    categoria= forms.ChoiceField(choices=CATEGORIA_CHOICES)

            

            
    