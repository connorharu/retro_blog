from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("começo da página do super famicom")
    return render(request, 'pagina_principal.html')

def sfc_main(request):
    return render(request, 'sfc_main.html')