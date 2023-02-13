from django.contrib import admin
from etudiants.models import Etudiant

class EtudiantAdmin(admin.ModelAdmin):
    list_display = ("nom","email","age")

admin.site.register(Etudiant,EtudiantAdmin)


# Register your models here.
