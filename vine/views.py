from django.shortcuts import render

def home(request):

    return render(request, 'vine/home.html')



def about(request):

    return render(request, 'vine/about.html')