from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import Augalas
from augalas.forms import AugaloForm


# Create your views here.
class AugalasDetailView(DetailView):
    model = Augalas



class AugalasListView(ListView):
    model = Augalas
    context_object_name = "augalai"
    paginate_by = 1
    template_name = "augalas_list"



class Naujas_augalo_View( FormView ):
    form_class = AugaloForm
    template_name = "augalas/naujas_augalas.html"
    success_url = "/augalai/"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
