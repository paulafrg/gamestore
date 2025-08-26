from gamestore.models import Rents
from django import forms

class RentForm(forms.ModelForm):
    class Meta:
        model = Rents
        fields = "__all__"
        widgets = {
            'customer': forms.Select(attrs={'class':'form-control'}),
            'game': forms.Select(attrs={'class':'form-control'}),
            'amount': forms.NumberInput(attrs={'class':'form-control', 'min':1}),
        }
    