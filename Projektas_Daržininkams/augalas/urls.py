from django.urls import path
from . import views
from .views import AugalasListView, Naujas_augalo_View, AugalasDetailView, search, succes_view, AugaloRedagavimasView

urlpatterns = [
    path('info/', views.pradinis, name='pradinis'),
    path('', AugalasListView.as_view(), name='augalo-info'),
    path("<int:pk>/", AugalasDetailView.as_view(), name="augalo-id"),
    path('naujas_augalas/', Naujas_augalo_View.as_view(), name='naujas-augalas'),
    path('augalo_redagavimas/<int:pk>/', AugaloRedagavimasView.as_view(), name='augalo_koregavimas'),
    path('augalo_panaikinimas/<int:pk>/', views.augalo_pasalinimas, name='augalo_pasalinimas'),
    path('succes/', succes_view, name='succes'),
    path('search/', search, name='search'),
]
