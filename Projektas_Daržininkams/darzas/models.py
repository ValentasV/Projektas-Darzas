from django.db import models
from augalas.models import Augalas
from vartotojai.models import Vartotojas


# Create your models here.

class Darzas(models.Model):
    augalas = models.ForeignKey(Augalas, on_delete=models.CASCADE)
    pikiavimo_data = models.DateTimeField(null=True, blank=True)
    persodinimo_vieta = models.CharField(max_length=100)
    augalo_uzsodinimo_plotas = models.CharField(max_length=100, verbose_name="augalo užsodinimo plotas", help_text="nurodyti skaičių arais")

    def __str__( self ):
        return f"{self.augalas}"

    class Meta:
        verbose_name = "Darzas"
        verbose_name_plural = "Daržas"


class DarzoDarbas(models.Model):
    pavadinimas = models.CharField(max_length=255)
    naudotojas = models.ForeignKey(Vartotojas, on_delete=models.CASCADE, null=True)
    def __str__( self ):
        return f"{self.pavadinimas}"
    class Meta:
        verbose_name = "Darzo Darbas"
        verbose_name_plural = "Daržo Darbai"
        unique_together = ('pavadinimas', 'naudotojas',)


class DarzoPrieziura(models.Model):
    darzas = models.ForeignKey(Darzas, on_delete=models.CASCADE)
    augalu_prieziuros_data = models.DateTimeField(verbose_name="augalų priežiūros data", null=True, blank=True)
    darzodarbai = models.ForeignKey(DarzoDarbas, verbose_name="Daržo darbai", on_delete=models.CASCADE)
    augalu_prieziuros_informacija = models.TextField(max_length=255, verbose_name="Parašykite detalesnę informaciją apie atliktą daržo priežiūros darbą", null=True, blank=True)
    pastabos = models.TextField(max_length=255, null=True, blank=True)

    def __str__( self ):
        return f"{self.darzas}"

    class Meta:
        verbose_name = "Darzo Prieziura"
        verbose_name_plural = "Daržo Priežiūra"


class DarzoDerlius(models.Model):
    augalas = models.ForeignKey(Augalas, on_delete=models.CASCADE)
    derliaus_nuemimo_data = models.DateTimeField(verbose_name="derliaus nuėmimo data", null=True, blank=True)
    derliaus_kiekis = models.TextField(max_length=100, null=True, blank=True)
    derliaus_sandeliavimo_vieta = models.CharField(max_length=225, verbose_name="derliaus sandėliavimo vieta", null=True, blank=True)
    derliaus_laikymo_laikotarpis = models.CharField(max_length=225, help_text="nurodyti kiek laiko laikėsi derlius", null=True, blank=True)

    def __str__( self ):
        return f"{self.augalas}"

    class Meta:
        verbose_name = "Darzo Derlius"
        verbose_name_plural = "Daržo Derlius"
