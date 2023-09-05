from django.urls import path
from .views import VartotojoRegistracijaView, VartotojoPrisijungimoView, pasisveikinimas_view, \
    VartotojoAtsijungimasView, VartotojoIstrynimasView

urlpatterns = [
    path("registracija/", VartotojoRegistracijaView.as_view(), name='registracijos_forma'),
    path("prisijungimas/", VartotojoPrisijungimoView.as_view(), name='prisijungimo_forma'),
    path('atsijungimas/', VartotojoAtsijungimasView.as_view(), name='atsijungimas'),
    path('istrynimas/', VartotojoIstrynimasView.as_view(), name='istrynimas'),
    path('pasisveikinimas/', pasisveikinimas_view, name='pasisveikinimas'),
]
