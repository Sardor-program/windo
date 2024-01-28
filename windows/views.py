from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')



def about(request):
    return render(request, 'about.html')


def farm(request):
    return render(request, 'farm.html')


def garden(request):
    return render(request, 'garden.html')


def dairy_product(request):
    return render(request, 'dairy.html')


def vegetables(request):
    return render(request, 'vegetable.html')


def fruit(request):
    return render(request, 'fruit.html')




