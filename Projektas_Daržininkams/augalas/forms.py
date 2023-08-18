from django import  forms
from django.forms import ModelForm
from .models import Augalas

class AugaloForm(ModelForm):
    class Meta:
        model = Augalas
        fields = ("kategorija",
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
            "kategorija": forms.TextInput(attrs={"class":"form-control", "placeholder": "Kategorija"}),
            "pavadinimas": forms.TextInput(attrs={"class": "form-control", "placeholder": "Pavadinimas"}),
            "veisle": forms.TextInput(attrs={"class":"form-control", "placeholder": "Veislė"}),
            "kiekis": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Kiekis"}),
            "talpos_dydis": forms.TextInput(attrs={"class":"form-control", "placeholder": "Talpos dysis"}),
            "sejimo_arba_sodinimo_data": forms.DateInput(attrs={"class":"form-control", "placeholder": "Sėjimo - sodnimo data (YYYY-MM-DD) formatu"}),
            "sejimo_arba_sodinimo_vieta": forms.TextInput(attrs={"class":"form-control", "placeholder": "Sėjimo - sodinimo vieta"}),
            "zemiu_rusis": forms.TextInput(attrs={"class":"form-control", "placeholder": "Žemių rūšis"}),
            "laistymo_budas": forms.TextInput(attrs={"class":"form-control", "placeholder": "Laistymo būdas"}),
            "pastabos": forms.TextInput(attrs={"class":"form-control", "placeholder": "Pastabos"})
        }
