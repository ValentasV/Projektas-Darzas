from django.urls import path

from daržas.views import naujas

urlpatterns = [
    path("du/", naujas),
]