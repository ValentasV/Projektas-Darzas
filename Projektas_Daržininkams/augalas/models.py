from django.db import models


# Create your models here.

class Augalas(models.Model):
    kategorija = models.CharField(help_text="Sėklos, Daigai, Gėlių sėklos, Sodinukai ir t.t", max_length=50)
    pavadinimas = models.CharField(help_text="Nurodykite augalo pavadinimą, pvz... agurkai, morkos ir t.t", max_length=50)
    veisle = models.CharField(help_text="Nurodykite augalo veislę", max_length=255, verbose_name="veislė")
    kiekis = models.IntegerField()
    talpos_dydis = models.CharField(max_length=50, help_text="Vazono talpa, pvz O,5 litro, 2 litrai",  null=True, blank=True)
    sejimo_data = models.DateTimeField(verbose_name="sėjimo - sodinimo data")
    sejimo_vieta = models.CharField(max_length=255, verbose_name="sėjimo vieta")
    zemiu_rusis = models.CharField(max_length=255, verbose_name="žemių rūšis", null=True, blank=True)
    pastabos = models.TextField(null=True, blank=True)


    def __str__( self ):
        return f"{self.veisle}"

    class Meta:
        verbose_name = "augalas"
        verbose_name_plural = "Augalai"




