from django import forms
from django.forms import ModelForm

from augalas.models import Augalas
from .models import Darzas, DarzoPrieziura, DarzoDerlius, DarzoDarbas


class DarzoForm(ModelForm):


    augalas = forms.ModelChoiceField(queryset=None)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DarzoForm, self).__init__(*args, **kwargs)
        self.fields["augalas"].queryset = Augalas.objects.filter(naudotojas=self.user)

    class Meta:
        model = Darzas
        fields = (
            "augalas",
            "pikiavimo_data",
            "persodinimo_vieta",
            "augalo_uzsodinimo_plotas"
            )

        labels = {
            "augalas": "",
            "pikiavimo_data": "",
            "persodinimo_vieta": "",
            "augalo_uzsodinimo_plotas": ""
        }

        widgets = {
            "augalas": forms.Select(choices="", attrs={"class":"form-control", "placeholder": "Augalai"}),
            "pikiavimo_data": forms.DateInput(attrs={"class":"form-control", "placeholder": "Pikiavimo data (YYYY-MM-DD) formatu"}),
            "persodinimo_vieta": forms.TextInput(attrs={"class":"form-control", "placeholder": "Persodinimo vieta"}),
            "augalo_uzsodinimo_plotas": forms.TextInput(attrs={"class": "form-control", "placeholder": "Augalo užsodinimo plotas"})
        }



class DarboForm(ModelForm):
    class Meta:
        model = DarzoDarbas
        fields = (
            "pavadinimas",
            )

        labels = {
            "pavadinimas": "",
        }

        widgets = {
            "pavadinimas": forms.TextInput(attrs={"class":"form-control", "placeholder": "Įtraukti naują daržo darbą"}),
        }




class DarzoPriuziurosForm(ModelForm):

    darzas = forms.ModelChoiceField(queryset=None, label="Augalai")
    darzodarbai = forms.ModelChoiceField(queryset=None, label="Daržo Darbai")
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DarzoPriuziurosForm, self).__init__(*args, **kwargs)
        self.fields["darzas"].queryset = Darzas.objects.filter(augalas__naudotojas=self.user)
        self.fields["darzodarbai"].queryset = DarzoDarbas.objects.filter(naudotojas=self.user)

    class Meta:
        model = DarzoPrieziura
        fields = (
            "darzas",
            "augalu_prieziuros_data",
            "darzodarbai",
            "augalu_prieziuros_informacija",
            "pastabos"
            )

        labels = {
            "darzas": "",
            "augalu_prieziuros_data": "",
            "darzodarbai": "",
            "augalu_prieziuros_informacija": "",
            "pastabos": ""
        }

        widgets = {
            "darzas": forms.Select(choices="", attrs={"class":"form-control", "placeholder": "Augalai"}),
            "augalu_prieziuros_data": forms.DateInput(attrs={"class":"form-control", "placeholder": "Augalų priežiūros data (YYYY-MM-DD) formatu"}),
            "darzodarbai": forms.Select(choices="", attrs={"class":"form-control", "placeholder": "Daržo darbas"}),
            "augalu_prieziuros_informacija": forms.TextInput(attrs={"class": "form-control", "placeholder": "Detalesnė informacija apie atliktą daržo darbą"}),
            "pastabos": forms.TextInput(attrs={"class": "form-control", "placeholder": "Pastabos"})
        }




class DarzoDerliausForm(ModelForm):

    augalas = forms.ModelChoiceField(queryset=None)
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DarzoDerliausForm, self).__init__(*args, **kwargs)
        self.fields["augalas"].queryset = Augalas.objects.filter(naudotojas=self.user)


    class Meta:
        model = DarzoDerlius
        fields = (
            "augalas",
            "derliaus_nuemimo_data",
            "derliaus_kiekis",
            "derliaus_sandeliavimo_vieta",
            "derliaus_laikymo_laikotarpis"
            )

        labels = {
            "augalas": "",
            "derliaus_nuemimo_data": "",
            "derliaus_kiekis": "",
            "derliaus_sandeliavimo_vieta": "",
            "derliaus_laikymo_laikotarpis": ""
        }

        widgets = {
            "augalas": forms.Select(choices="", attrs={"class":"form-control", "placeholder": "Augalai"}),
            "derliaus_nuemimo_data": forms.DateInput(attrs={"class":"form-control", "placeholder": "Derliaus nuėmimo data (YYYY-MM-DD) formatu"}),
            "derliaus_kiekis": forms.TextInput(attrs={"class":"form-control", "placeholder": "Derliaus kiekis"}),
            "derliaus_sandeliavimo_vieta": forms.TextInput(attrs={"class": "form-control", "placeholder": "Derliaus sandėliavimo vieta"}),
            "derliaus_laikymo_laikotarpis": forms.TextInput(attrs={"class": "form-control", "placeholder": "nurodyti kiek laiko derlius bus laikomas"})
        }
