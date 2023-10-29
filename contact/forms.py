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
                    'class': 'form-control border-1 border-warning shadow-lg',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-lg',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control border-1 border-warning shadow-lg',
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

            # raise ValidationError(
            #     'não digite ABC neste campo',
            #     code='invalid' 
            # )
            self.add_error(
                'first_name',
                ValidationError(
                    ' ❌ Veio do add_erro',
                    code='invalid'
                )
            )


        return first_name
