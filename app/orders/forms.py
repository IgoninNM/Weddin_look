from django import forms


from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}))
    phoneNumber = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': '8-800-000-00-00'
    }))

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'phoneNumber')
