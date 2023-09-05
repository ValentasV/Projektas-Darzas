from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from darzas.models import DarzoPrieziura
from .models import Augalas
from augalas.forms import AugaloForm

def pradinis(request):
    return render(request, 'augalas/pradinis.html')
# Create your views here.

class AugalasDetailView(LoginRequiredMixin, DetailView):
    model = Augalas
    template_name = "augalas/augalas_detail.html"
    def get_queryset(self):
        return Augalas.objects.filter(naudotojas=self.request.user)


class AugalasListView(LoginRequiredMixin, ListView):
    model = Augalas
    context_object_name = "augalai"
    paginate_by = 3
    template_name = "augalas_list"
    ordering = ['pavadinimas']
    def get_queryset(self):
         return Augalas.objects.filter(naudotojas=self.request.user)


def succes_view(request):
    return render(request, "augalas/succes.html")

class Naujas_augalo_View(LoginRequiredMixin, FormView ):
    form_class = AugaloForm
    template_name = "augalas/naujas_augalas.html"
    success_url = "/augalai/succes/"
    def form_valid(self, form):
        form.instance.naudotojas=self.request.user
        form.save()
        return super().form_valid(form)
    def get_queryset(self):
        return Augalas.objects.filter(naudotojas=self.request.user)

@login_required
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        augalas = Augalas.objects.filter(Q(pavadinimas__icontains=searched) | Q(veisle__icontains=searched))
        darzodarbas = DarzoPrieziura.objects.filter(darzodarbai__pavadinimas__icontains=searched)
        return render(request, "augalas/search.html", {"searched": searched, "augalas": augalas, "darzodarbas":darzodarbas})
    else:
        return render(request, "augalas/search.html", {})

@login_required
def augalo_redagavimas(request, pk):
    augalas = Augalas.objects.get(pk=pk)
    if request.method == 'POST':
        form = AugaloForm(request.POST, instance=augalas)
        if form.is_valid():
            form.save()
    else:
        form = AugaloForm(instance=augalas)
    return render(request, 'augalas/augalo_redagavimas.html', {'form': form})

@login_required
def augalo_pasalinimas(request, pk):
    augalas = get_object_or_404(Augalas, pk=pk)
    if request.method == 'POST':
        augalas.delete()
        return redirect("augalo-info")
