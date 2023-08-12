from django.urls import path
from .views import DarzasListView

urlpatterns = [
    path("info/", DarzasListView.as_view(), name='darzo-info'),
]
