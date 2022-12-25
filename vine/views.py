from django.shortcuts import render

def home(request):

    return render(request, 'vine/home.html')



def about(request):

    return render(request, 'vine/about.html')


def services(request):

    return render(request, 'vine/services.html')



def contact(request):

    return render(request, 'vine/contact.html')


def store(request):
    return render(request, 'vine/store.html')
