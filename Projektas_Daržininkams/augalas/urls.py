from django.urls import path
from .views import AugalasListView, Naujas_augalo_View, AugalasDetailView

urlpatterns = [
    path('', AugalasListView.as_view(), name='augalo-info'),
    path("<int:pk>/", AugalasDetailView.as_view(), name="augalo-id"),
    path('naujas_augalas/', Naujas_augalo_View.as_view(), name='naujas-augalas'),
]
