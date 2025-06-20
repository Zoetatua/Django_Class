from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def me(request):
    return render(request, 'Kaizo.html')

def contact(request):
    return render(request, 'Contact.html')