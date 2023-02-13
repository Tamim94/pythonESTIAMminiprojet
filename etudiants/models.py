from django.db import models
from django.core.validators import *

class Etudiant(models.Model):
    nom = models.fields.CharField(max_length=100)
    email = models.fields.CharField(max_length=100)
    age = models.fields.IntegerField(validators=[MinValueValidator(18),MaxValueValidator(40)])

    def __str__(self):
        return "{} ({}, {})".format(self.nom,self.email,self.age)