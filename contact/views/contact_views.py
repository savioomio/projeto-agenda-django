from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact
from django.contrib.auth.decorators import login_required

@login_required(login_url='contact:login')
def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .order_by('-id')

    # paginação dos contatos
    paginator = Paginator(contacts, 25)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos',
    }

    return render(
        request,
        'contact/index.html',
        context
    )

@login_required(login_url='contact:login')
def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects \
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=search_value) |
            Q(last_name__icontains=search_value) 
        )\
        .order_by('-id')
    
    paginator = Paginator(contacts, 25)  
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'search',
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context
    )


@login_required(login_url='contact:login')
def contact(request, contact_id):
    site_title = "Nenhum contato"
    try:
        contact = Contact.objects.get(pk=contact_id)    
        if contact:    
            saida_contato = "Este ID possui contato"
            site_title = f'{contact.first_name} {contact.last_name}'
    except :
        contact = "Sem registro"
        saida_contato = f'O ID"{contact_id}" não possui um contato!'

    context = {
        'contact': contact,
        'site_title': site_title,
        'saida_contato': saida_contato,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
