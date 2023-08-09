from django.contrib import admin
from augalas.models import Augalas



class AugalasAdmin(admin.ModelAdmin): # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["kategorija",
                    "pavadinimas",
                    "veisle",
                    "kiekis",
                    "talpos_dydis",
                    "sejimo_data",
                    "sejimo_vieta",
                    "zemiu_rusis",
                    "pastabos"]



# Išfiltruoja variantus pagal pasirinktą kriterijų
    list_filter = ["kategorija", "pavadinimas", "veisle"]

# Kuomet vykdysime filtaciją mums išmes visus Variantus pagal pasirinktą fitracijos kriterijų
    search_fields = ["kategorija", "pavadinimas", "veisle"]




# Register your models here.
admin.site.register(Augalas, AugalasAdmin)