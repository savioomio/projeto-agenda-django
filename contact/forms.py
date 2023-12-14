from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 
            'username', 'password1', 'password2',
        ]
    first_name = forms.CharField(
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )
    last_name = forms.CharField( 
        required=True,
        min_length=3,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )
    password1 = forms.CharField(
        label="Senha",  
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )
    password2 = forms.CharField(
        label="Confirme a Senha",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-4'
            }
        )
    )
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )

        return email

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='*',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        ),
        error_messages={
            'min_length': 'Please, add more than 2 letters.'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='*', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )
    username = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='*', 
        widget=forms.TextInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )
    email = forms.CharField(
        required=True,
        help_text='*', 
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        )
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'form-control border-1 border-warning shadow-big mb-2'
            }
        ),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2⠀",
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                'class': 'form-control border-1 border-warning shadow-big mb-4'
            }
        ),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control border-1 border-warning shadow-big mb-2',
                'accept': 'image/*',
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 
            'last_name', 
            'phone',  
            'email', 
            'category',
            'picture',
            'description',
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
