from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',  
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big',
                }
            ),
        }

    def clean(self):
        cleaned_data = self.cleaned_data

        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )
            
        self.add_error(
            'last_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()
