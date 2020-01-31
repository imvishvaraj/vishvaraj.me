from django.shortcuts import render


def homepage(request):
    return render(request, 'jobs/home.html')


def homepage2(request):
    return render(request, 'jobs/home2.html')

def home3(request):
    return render(request, 'jobs/index.html')
