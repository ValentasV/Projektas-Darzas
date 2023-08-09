from django.urls import path
from .views import AugalasListView, Naujas_augalo_View, AugalasView

urlpatterns = [
    path('augalai/<int:pk>/', AugalasListView.as_view(), name='augalo-info'),
    path("<int:pk>/", AugalasView.as_view(), name="augalo-id"),
    path('naujas_augalas/', Naujas_augalo_View.as_view(), name='naujas-augalas'),
]
