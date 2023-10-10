from django.shortcuts import get_object_or_404, render, redirect
from contact.models import Contact

def create(request):

    context = {
        
    }

    return render(
        request,
        'contact/create.html',
        context
    )