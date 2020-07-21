from django.shortcuts import render


def home(request):
    return render(request, 'launch_page/home_new.html')
