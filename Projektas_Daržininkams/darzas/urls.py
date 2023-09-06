from django.urls import path

from . import views
from .views import DarzasListView, DarzoPrieziuraListView, DarzoDerliusListView, DarzasDetailView, \
    DarzoPrieziuraDetailView, DarzoDerliusDetailView, NaujasDarzasView, NaujaPrieziuiraView, AugaluDerliusView, \
    DarzoDarbasListView, PridetiDarbaView, DarzoDarbasDetailView

urlpatterns = [
    path("darzas/", DarzasListView.as_view(), name='darzo-info'),
    path("<int:pk>/", DarzasDetailView.as_view(), name="darzo-id"),
    path('naujas_darzas/', NaujasDarzasView.as_view(), name='naujas-darzas'),
    path('darzo_redagavimas/<int:pk>/', views.darzo_redagavimas, name='darzo_koregavimas'),
    path('darzo_panaikinimas/<int:pk>/', views.darzo_pasalinimas, name='darzo_pasalinimas'),

    path('darzo_darbas/', DarzoDarbasListView.as_view(), name='darbai'),
    path("<int:pk>/", DarzoDarbasDetailView.as_view(), name="darbo-id"),
    path('naujas_darbas/', PridetiDarbaView.as_view(), name='naujas-darbas'),
    path('darbo_redagavimas/<int:pk>/', views.darbo_redagavimas, name='darbo_koregavimas'),
    path('darbo_panaikinimas/<int:pk>/', views.darbo_pasalinimas, name='darbo_pasalinimas'),


    path('darzo_prieziura/', DarzoPrieziuraListView.as_view(), name='darzo_darbai'),
    path("<int:pk>/darbai/", DarzoPrieziuraDetailView.as_view(), name="darzo_darbu_id"),
    path('nauja_prieziura/', NaujaPrieziuiraView.as_view(), name='nauja-prieziura'),
    path('darzo_prieziura_redagavimas/<int:pk>/', views.prieziuros_redagavimas, name='darzo_prieziuros_redagavimas'),
    path('darzo_prieziuros_panaikinimas/<int:pk>/', views.darzo_prieziuros_pasalinimas, name='prieziuros_pasalinimas'),

    path('darzo_derlius/', DarzoDerliusListView.as_view(), name='derlius'),
    path("<int:pk>/derlius/", DarzoDerliusDetailView.as_view(), name="derliaus_id"),
    path("prideti_derliu/", AugaluDerliusView.as_view(), name="naujas_derlius"),
    path('darzo_derliaus_redagavimas/<int:pk>/', views.derliaus_redagavimas, name='darzo_derliaus_redagavimas'),
    path('darzo_derliaus_panaikinimas/<int:pk>/', views.darzo_derliaus_pasalinimas, name='derliaus_pasalinimas'),
]

