from django import forms
from .models import Owner


class AddOwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = '__all__'
