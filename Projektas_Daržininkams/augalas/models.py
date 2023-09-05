from django.db import models
from vartotojai.models import Vartotojas


# Create your models here.

class Augalas(models.Model):
    kategorija = models.CharField(help_text="Sėklos, Daigai, Gėlių sėklos, Sodinukai ir t.t", max_length=50)
    pavadinimas = models.CharField(help_text="Nurodykite augalo pavadinimą, pvz... agurkai, morkos ir t.t", max_length=50)
    veisle = models.CharField(help_text="Nurodykite augalo veislę", max_length=255, verbose_name="veislė")
    kiekis = models.IntegerField()
    talpos_dydis = models.CharField(max_length=50, help_text="Vazono talpa, pvz O,5 litro, 2 litrai",  null=True, blank=True)
    sejimo_arba_sodinimo_data = models.DateTimeField(verbose_name="sėjimo - sodinimo data")
    sejimo_arba_sodinimo_vieta = models.CharField(max_length=120, verbose_name="sėjimo - sodinimo vieta")
    zemiu_rusis = models.CharField(max_length=120, verbose_name="žemių rūšis", null=True, blank=True)
    laistymo_budas = models.CharField(max_length=225, verbose_name="laistymo būdas", help_text="kapiliarinis laistymas, laistymas iš šlangos ir t.t. ")
    pastabos = models.TextField(max_length=255, null=True, blank=True)
    naudotojas = models.ForeignKey(Vartotojas, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(null=True, blank=True, upload_to="augalo_nuotraukos")



    def __str__( self ):
        return f"{self.pavadinimas} {self.veisle}"

    class Meta:
        verbose_name = "augalas"
        verbose_name_plural = "Augalai"
        unique_together = ('pavadinimas', 'veisle',)




