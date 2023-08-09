from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Augalas


# Create your views here.
class AugalasView(View):
    model = Augalas



class AugalasListView(ListView):
    model = Augalas
    context_object_name = "augalai"
    paginate_by = 1
    template_name = "augalas_list"



class Naujas_augalo_View( View ):
    def get(self, request):
        return render(
            request,
            "augalas/naujas_augalas.html"
        )

        # 1. Pasitikrinti ar viskas suvesta teisingai. Nurodome reikšmes tikrinimui
    def post(self, request):
        reiksmes = {
            'kategorija': 'augalo kategorija',
            'pavadinimas': 'augalo pavadinimas',
            'veisle': 'augalo veislė',
            'kiekis': 'augalo kiekis',
            'talpos_dydis': 'augalo talpos dydis',
            'sejimo_data': 'augalo sėjimo data',
            'sejimo_vieta': 'augalo sėjimo vieta',
            'zemiu_rusis': 'augalo žemės rūšis',
            'pastabos': 'pastabos'
        }

        # 2. Nurodom privalomas reikšmes. Neužpildžius šių reikšmių negalima bus pridėti naujo augalo.
        privalomos_reiksmes = [
            'kategorija',
            'pavadinimas',
            'veisle',
            'kiekis',
            'sejimo_data',
            'sejimo_vieta',

        ]

        # 3. Patikrinam ar reikalingos reikšmės užpildytos laukeliuose
        augalas = Augalas()
        for key, value in reiksmes.items():
            if key in privalomos_reiksmes and len(request.POST.get(key)) == 0:
                messages.error(request, f"Reikia įvesti {value}")
                return redirect("/augalas/naujas_augalas")
            else:
                setattr(augalas, key, request.POST.get(key))


        # 4. Išsaugom naują augalą duomenų bazėje
        augalas.save()

        # 4. Po naujoo augalo įtraukimo į duomenų bazę vartotojas gražinamas į pradinį augalų sąrašo puslapi.
        return redirect(f"/augalas/augalai/{augalas.id}/")
#
