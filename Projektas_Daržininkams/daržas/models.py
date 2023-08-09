from django.db import models
from augalas.models import Augalas


# Create your models here.

class Darzas(models.Model):
    augalas = models.ForeignKey(Augalas, on_delete=models.CASCADE)
    pikiavimo_data = models.DateTimeField(null=True, blank=True)
    daigu_sodinimo_data = models.DateTimeField(verbose_name="daigų sodinimo data", null=True, blank=True)
    persodinimo_vieta = models.CharField(max_length=100)
    augalo_uzsodinimo_plotas = models.CharField(max_length=100, verbose_name="augalo užsodinimo plotas", help_text="nurodyti skaičių arais")
    laistymo_budas = models.CharField(max_length=225, verbose_name="laistymo būdas", help_text="kapiliarinis laistymas, laistymas iš šlangos ir t.t. ")
    vandens_kiekis_reikalingas_augalams = models.IntegerField(help_text="nurodykite litrais")
    derliaus_nuemimo_data = models.DateTimeField(verbose_name="derliaus nuėmimo data", null=True, blank=True)
    derliaus_kiekis = models.TextField()
    derliaus_sandeliavimo_vieta = models.CharField(max_length=225, verbose_name="derliaus sandėliavimo vieta")
    derliaus_laikymo_laikotarpis = models.CharField(max_length=225, help_text="nurodyti kiek laiko laikėsi derlius", null=True, blank=True)

    def __str__( self ):
        return f"{self.augalas}"

    class Meta:
        verbose_name = "Darzas"
        verbose_name_plural = "daržas"




class DarzoDarbas(models.Model):
    darzas = models.ForeignKey(Darzas, on_delete=models.CASCADE)
    augalu_prieziuros_data = models.DateTimeField(verbose_name="augalų priežiūros data", null=True, blank=True)
    trasos = models.CharField(max_length=255, verbose_name="trąšų pavadinimas", null=True, blank=True)
    augalu_ligos = models.CharField(max_length=255, verbose_name="augalų ligos", help_text="nurodykite kokiomis ligomis sirgo augalai", null=True, blank=True)
    pesticidai = models.CharField(max_length=255, verbose_name="pesticidų pavadinimas", null=True, blank=True)
    trasu_ir_pesticidu_informacija = models.TextField(verbose_name="trašų ir pesticidų panaudojimo informacija", null=True, blank=True )
    ravejimas = models.CharField(max_length=255, verbose_name="ravėjimas", help_text="parašykite ką ir kada ravėjote", null=True, blank=True)
    dangos_ir_pleveles = models.CharField(max_length=255, verbose_name="dangos ir plėvelės", help_text="nurodykite kokias dangas naudojote; agrodanga, agroplėvelė ir t.t.", null=True, blank=True)
    pastabos = models.TextField(null=True, blank=True)

    def __str__( self ):
        return f"{self.darzas}"

    class Meta:
        verbose_name = "Darzo Darbas"
        verbose_name_plural = "Daržo darbai"

