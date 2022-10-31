from . models import products
from django import forms
class ModeForm(forms.ModelForm):
    class Meta:
        model = products
        fields=['name','desc','price','offer','image']