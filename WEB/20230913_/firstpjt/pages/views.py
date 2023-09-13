from django.shortcuts import render

# Create your views here.
def index(request, name):
    context = {
        'name' : name
    }
    return render(request, 'pages/index.html', context)