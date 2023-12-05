from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado com sucesso')
            return redirect('contact:login')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'site_title': "Register User",
        }
    )

class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapAuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control border-1 border-warning shadow-big mb-2'})
        self.fields['password'].widget.attrs.update({'class': 'form-control border-1 border-warning shadow-big mb-4'})

def login_view(request):
    form = BootstrapAuthenticationForm(request)

    if request.method == 'POST':
        form = BootstrapAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            print(user) 
            messages.success(request, 'Logado com sucesso!')
            return redirect('contact:index')
        messages.error(request, 'Login inválido')
    
    return render(
        request,
        'contact/login.html',
        {
            'form': form,
            'site_title': "Login User",
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')