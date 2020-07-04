from django.db import models
from django.urls import reverse


class Proprietaire(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    tel = models.CharField(max_length=8, unique=True)
    mail = models.CharField(max_length=100)

    def __repr__(self):
        return f"Proprietaire('{self.nom}', '{self.prenom}', '{self.tel}', \
            '{self.mail}')"
    
    def __str__(self):
        return self.nom+" "+self.prenom
    
    def get_absolute_url(self):
        return reverse("detail-owner", kwargs={"pk": self.pk})