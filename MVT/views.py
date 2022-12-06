from django.shortcuts import render
from MVT.models import Familiar

# Create your views here.

def index(request):
    return render(request, "MVT/Familia.html")

def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "MVT/Familia.html", {"lista_familiares": lista_familiares})


