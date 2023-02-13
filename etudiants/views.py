from django.shortcuts import render
from django.http import HttpResponse
from etudiants.models import Etudiant

def index(request):
    etudiants = Etudiant.objects.all()
    obj = {
        "x" : "Estiamflix",
        "y" : 100,
        "liste" : etudiants
    }
    return render(request, "etudiants/index.html", obj)

def about(request):
    return HttpResponse("<h1>Bienvenu dans about</h1>")

def etudiantShow(request, id):
	e = Etudiant.objects.get(id=id)

	return render(request, "etudiants/etudiant-show.html", {'e':e})

