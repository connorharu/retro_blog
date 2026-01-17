from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wii_main(request):
    return render(request, 'wii_main.html')