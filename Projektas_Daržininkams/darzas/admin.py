from django.contrib import admin
from darzas.models import Darzas, DarzoDarbas, DarzoPrieziura


# Register your models here.

class DarzasAdmin(admin.ModelAdmin):

    # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["augalo_uzsodinimo_plotas",
                    "persodinimo_vieta",
                    "derliaus_nuemimo_data"]


    # Išfiltruoja variantus pagal pasirinktą kriterijų
    list_filter = ["derliaus_nuemimo_data",
                   "persodinimo_vieta"]

    # Kuomet vykdysime filtaciją mums išmes visus Variantus pagal pasirinktą fitracijos kriterijų
    search_fields = ["derliaus_sandeliavimo_vieta"]



class DarzoDarbasAdmin(admin.ModelAdmin):

    # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["pavadinimas"]

class DarzoPrieziuraAdmin(admin.ModelAdmin):

    # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["augalu_prieziuros_data",
                    "darzodarbas",
                    "pastabos"]

    # Išfiltruoja variantus pagal pasirinktą kriterijų
    list_filter = ["augalu_prieziuros_data",
                   "darzodarbas"]

    # Kuomet vykdysime filtaciją mums išmes visus Variantus pagal pasirinktą fitracijos kriterijų
    search_fields = ["darzodarbas"]

# Užregistruojam savo modelius admino puslapyje
admin.site.register(Darzas, DarzasAdmin)
admin.site.register(DarzoDarbas, DarzoDarbasAdmin)
admin.site.register(DarzoPrieziura, DarzoPrieziuraAdmin)