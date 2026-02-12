from django.contrib.auth.models import User
from django.db import models

class Salle(models.Model):
    nom = models.CharField(max_length=100)
    capacite = models.IntegerField()
    localisation = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    date = models.DateField()
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()

    def __str__(self):
        return f"{self.user.username} - {self.salle.nom}"
