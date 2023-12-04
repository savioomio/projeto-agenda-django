from django.shortcuts import render
from django.contrib import messages
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado com sucesso')

    return render(
        request,
        'contact/register.html',
        {
            'form': form,
            'site_title': "Register User",
        }
    )