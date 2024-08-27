from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'section_title' : 'Muebles tipo',

    }
    return render(request, 'myapp/index.html', context)