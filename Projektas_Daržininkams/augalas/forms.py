from django import forms
from django.forms import ModelForm
from .models import Augalas



class AugaloForm(ModelForm):
    class Meta:
        model = Augalas
        fields = ("nuotrauka",
                  "kategorija",
                  "pavadinimas",
                  "veisle",
                  "kiekis",
                  "talpos_dydis",
                  "sejimo_arba_sodinimo_data",
                  "sejimo_arba_sodinimo_vieta",
                  "zemiu_rusis",
                  "laistymo_budas",
                  "pastabos")

        labels = {
            "kategorija": "",
            "pavadinimas": "",
            "veisle": "",
            "kiekis": "",
            "talpos_dydis": "",
            "sejimo_arba_sodinimo_data": "",
            "sejimo_arba_sodinimo_vieta": "",
            "zemiu_rusis": "",
            "laistymo_budas": "",
            "pastabos": ""
        }

        widgets = {
            "kategorija": forms.TextInput(attrs={"class":"form-control", "placeholder": "Augalo Kategorija - sėklos, daigai, sodinukai... "}),
            "pavadinimas": forms.TextInput(attrs={"class": "form-control", "placeholder": "Augalo Pavadinimas - morkos, obuoliai..."}),
            "veisle": forms.TextInput(attrs={"class":"form-control", "placeholder": "Augalo Veislė"}),
            "kiekis": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Kiekis"}),
            "talpos_dydis": forms.TextInput(attrs={"class":"form-control", "placeholder": "Sėjamo ar sodinamo augalo talpos dydis"}),
            "sejimo_arba_sodinimo_data": forms.DateInput(attrs={"class":"form-control", "placeholder": "Sėjimo - sodinimo data (YYYY-MM-DD) formatu"}),
            "sejimo_arba_sodinimo_vieta": forms.TextInput(attrs={"class":"form-control", "placeholder": "Sėjimo - sodinimo vieta"}),
            "zemiu_rusis": forms.TextInput(attrs={"class":"form-control", "placeholder": "Žemių rūšis"}),
            "laistymo_budas": forms.TextInput(attrs={"class":"form-control", "placeholder": "Laistymo būdas - purkštuvas, laistymo sistema..."}),
            "pastabos": forms.TextInput(attrs={"class":"form-control", "placeholder": "Pastabos"})
        }


