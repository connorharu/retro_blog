from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tds_main(request):
    return render(request, '3ds_main.html')