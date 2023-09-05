from django.contrib import admin
from darzas.models import Darzas, DarzoPrieziura, DarzoDerlius, DarzoDarbas


# Register your models here.

class DarzasAdmin(admin.ModelAdmin):

    # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["augalas",
                    "augalo_uzsodinimo_plotas",
                    "persodinimo_vieta",
                    ]


    # Išfiltruoja variantus pagal pasirinktą kriterijų
    list_filter = ["augalas",
                   "persodinimo_vieta"]

    # Kuomet vykdysime filtaciją mums išmes visus Variantus pagal pasirinktą fitracijos kriterijų
    search_fields = ["augalas__pavadinimas",
                     "augalas__veisle",
                     "persodinimo_vieta"]



class DarzoDarbasAdmin(admin.ModelAdmin):

    # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["pavadinimas"]

class DarzoPrieziuraAdmin(admin.ModelAdmin):

    def augalas(self, model):
        return f"{model.darzas.augalas.pavadinimas} {model.darzas.augalas.veisle}"

    # Admino puslapyje nurodom kokius klasės modelius norime, kad mums rodytu lentelė
    list_display = ["augalas",
                    "augalu_prieziuros_data",
                    "darzodarbai",
                    "pastabos"]

    # Išfiltruoja variantus pagal pasirinktą kriterijų
    list_filter = ["augalu_prieziuros_data",
                   "darzodarbai"]

    # Kuomet vykdysime filtaciją mums išmes visus Variantus pagal pasirinktą fitracijos kriterijų
    search_fields = ["darzodarbai"]


class DarzoDerliusAdmin(admin.ModelAdmin):

    list_display = ["augalas",
                    "derliaus_nuemimo_data",
                    "derliaus_kiekis",
                    "derliaus_sandeliavimo_vieta",
                    "derliaus_laikymo_laikotarpis"]

    # Išfiltruoja variantus pagal pasirinktą kriterijų
    list_filter = ["augalas",
                   "derliaus_sandeliavimo_vieta"]

    search_fields = ["augalas__pavadinimas",
                     "augalas__veisle",
                     "derliaus_sandeliavimo_vieta"]


# Užregistruojam savo modelius admino puslapyje
admin.site.register(Darzas, DarzasAdmin)
admin.site.register(DarzoDarbas, DarzoDarbasAdmin)
admin.site.register(DarzoPrieziura, DarzoPrieziuraAdmin)
admin.site.register(DarzoDerlius, DarzoDerliusAdmin)
