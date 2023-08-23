from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from vartotojai.models import Vartotojas


# Create your views here.

class VartotojoRegistracijaView(View):
    def get(self, request):
        return render(request, "registracija/registracija.html")

    def post(self, request):
        vardas = request.POST.get("Vardas")
        pavarde = request.POST.get("Pavarde")
        telefonas = request.POST.get("Telefonas")
        elektroninis_pastas = request.POST.get("elektroninis_pastas")
        password = request.POST.get("slaptažodis")
        try:
            Vartotojas.objects.get(elektroninis_pastas=elektroninis_pastas)
            return render(request, "registracija/registracija.html",
                          {"klaida": "Vartotojas su tokiu elektroniniu paštu jau egzistuoja"})
        except Vartotojas.DoesNotExist:
            pass

        vartotojas = Vartotojas(vardas=vardas, pavarde=pavarde, telefonas=telefonas,
                                elektroninis_pastas=elektroninis_pastas)
        vartotojas.set_password(password)
        vartotojas.save()
        return redirect(reverse("registracijos_forma"))



class VartotojoPrisijungimoView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "prisijungimas.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            elektroninis_pastas = form.cleaned_data.get("elektroninis_pastas")
            password = form.cleaned_data.get("password")
            user = Vartotojas.objects.get(elektroninis_pastas=elektroninis_pastas)
            if user.check_password(password):
                # Log in the user
                return redirect("pradinis.html")
            else:
                form.add_error(None, "Neteisingas slaptažodis")
        return render(request, "prisijungimas.html", {"form": form})