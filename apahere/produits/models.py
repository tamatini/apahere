from django.db import models
from proprietaire.models import Proprietaire


class Biens(models.Model):
    type_de_biens = (
        ('appartement','appartement'),
        ('maison','maison'),
        ('terrain','terrain')
    )
    
    type_operation = (
        ('vente','vente'),
        ('location','location'),
        ('estimation','estimation')
    )

    reponse_boolean = (
        ('oui','oui'),
        ('non','non')
    )

    type_de_bien = models.CharField(max_length=50, choices=type_de_biens)
    operation = models.CharField(max_length=50, choices=type_operation)
    chambre = models.IntegerField()
    sdb = models.IntegerField()
    toilette = models.IntegerField()
    superficie_salon = models.IntegerField()
    cuisine = models.IntegerField()
    meuble = models.CharField(max_length=3, choices=reponse_boolean)
    garage = models.CharField(max_length=3, choices=reponse_boolean)
    parking = models.IntegerField()
    superficie_habitat = models.IntegerField()
    superficie_terrain = models.IntegerField()
    proprietaire = models.ForeignKey(Proprietaire, on_delete=models.CASCADE)


    def __repr__(self):
        return f"Biens('{self.id}','{self.type_de_bien}','{self.operation}','{self.chambre}', \
            '{self.sdb}','{self.toilette}','{self.superficie_salon}','{self.cuisine}', \
                '{self.meuble}', '{self.garage}', '{self.parking}', '{self.superficie_habitat}', \
                    '{self.superficie_terrain}')"


class Photo_biens(models.Model):
    bien = models.ForeignKey(Biens, on_delete=models.CASCADE, null=True)
    images = models.ImageField(upload_to="static/img/biens_img")

    def __str__(self):
        return f"{self.id}"