from django.shortcuts import render

def index(request):
    context = {
        'teste': 'tetsejjfjfsdadadasjfjfj',
    }

    return render(
        request,
        'contact/index.html',
        context
    )
    


