from django import forms
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su apellido'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Ingrese su email'}),
            }