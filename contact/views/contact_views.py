from django.shortcuts import render
from contact.models import contact

def index(request):
    contacts = contact.objects.filter(show=True).order_by('-id')[:20]

    context = {
        'contacts': contacts,
    }
    return render(
        request,
        'contact/index.html',
        context,
    )