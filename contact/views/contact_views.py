from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact
# from django.http import JsonResponse
# from django.template.loader import render_to_string


def index(request):
    contacts = Contact.objects \
        .filter(show=True)\
        .order_by('-id')

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

# def search(request):
#     search_value = request.GET.get('q', '').strip()

#     if search_value == '':
#         # Lida com o caso de pesquisa vazia, se necessário
#         return JsonResponse({'results': ''})  # Retorna uma string vazia

#     contacts = Contact.objects \
#         .filter(show=True) \
#         .filter(
#             Q(first_name__contains=search_value) |
#             Q(last_name__contains=search_value)
#         ) \
#         .order_by('first_name')

#     # Renderiza apenas a parte dos resultados como HTML
#     result_html = render_to_string('contact/search_results.html', {'contacts': contacts})

#     return JsonResponse({'results': result_html})

def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    single_contact = get_object_or_404(
        Contact, pk=contact_id, show=True
    )

    site_title = f'{single_contact.first_name} {single_contact.last_name}'

    context = {
        'contact': single_contact,
        'site_title': site_title,
    }

    return render(
        request,
        'contact/contact.html',
        context
    )