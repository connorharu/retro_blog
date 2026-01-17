from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def ps2_main(request):
    return render(request, 'ps2_main.html')