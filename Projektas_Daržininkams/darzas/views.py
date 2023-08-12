from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from darzas.models import Darzas


# Create your views here.

class DarzasListView(ListView):
    model = Darzas
    context_object_name = "darzas"
    template_name = "darzas_list"
    paginate_by = 1

