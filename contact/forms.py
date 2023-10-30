from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',  
            'email', 'category', 'description', 
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big mb-2',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big mb-2',
                }
            ),
            'phone': forms.NumberInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big mb-2',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big mb-2',
                }
            ),
            'category': forms.Select(
                attrs={
                    'class': 'form-select border-1 border-warning shadow-big mb-2 ',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-big mb-3',
                }
            ),

        }

    def clean(self):
        
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                '❌ Primeiro nome não pode ser igual o segundo',
                code='invalid'
            )  
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':

            self.add_error(
                'first_name',
                ValidationError(
                    ' ❌ Não pode colocar ABC no primeiro nome',
                    code='invalid'
                )
            )


        return first_name
