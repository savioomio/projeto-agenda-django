from django.shortcuts import render

def home(request):
    context = {
        'teste': 'tetsejjfjfsdadadasjfjfj',
    }

    return render(
        request,
        'home.html',
        context
    )
    


