from django.urls import path

from vartotojai.views import VartotojoRegistracijaView, VartotojoPrisijungimoView

urlpatterns = [
    path("registracija/", VartotojoRegistracijaView.as_view(), name='registracijos_forma'),
    path("prisijungimas/", VartotojoPrisijungimoView.as_view(), name='prisijungimo_forma'),
]