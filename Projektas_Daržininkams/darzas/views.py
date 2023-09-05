from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, FormView
from darzas.forms import DarzoForm, DarzoPriuziurosForm, DarzoDerliausForm, DarboForm
from darzas.models import Darzas, DarzoPrieziura, DarzoDerlius, DarzoDarbas


# Create your views here.

class DarzasListView(LoginRequiredMixin, ListView):
    model = Darzas
    context_object_name = "darzas"
    template_name = "darzas/darzas_list"
    paginate_by = 3
    def get_queryset(self):
        return Darzas.objects.filter(augalas__naudotojas=self.request.user)

class DarzasDetailView(LoginRequiredMixin, DetailView):
    model = Darzas
    template_name = "darzas/darzas_detail.html"
    def get_queryset(self):
        return Darzas.objects.filter(augalas__naudotojas=self.request.user)

class NaujasDarzasView(LoginRequiredMixin, FormView):
    form_class = DarzoForm
    template_name = "darzas/naujas_darzas.html"
    success_url = "/augalai/succes/"
    def form_valid(self, form):
        form.instance.naudotojas=self.request.user
        form.save()
        return super().form_valid(form)
    def get_queryset(self):
        return Darzas.objects.filter(augalas__naudotojas=self.request.user)

@login_required
def darzo_redagavimas(request, pk):
    darzas = Darzas.objects.get(pk=pk)
    if request.method == 'POST':
        form = DarzoForm(request.POST, instance=darzas)
        if form.is_valid():
            form.save()
    else:
        form = DarzoForm(instance=darzas)
    return render(request, 'darzas/darzo_redagavimas.html', {'form': form})

@login_required
def darzo_pasalinimas(request, pk):
    augalas = get_object_or_404(Darzas, pk=pk)
    if request.method == 'POST':
        augalas.delete()
        return redirect("darzo-info")




class DarzoDarbasListView(LoginRequiredMixin, ListView):
    model = DarzoDarbas
    template_name = "darzas/darzo_darbas_list.html"
    context_object_name = "darbai"
    paginate_by = 3
    def get_queryset(self):
        return DarzoDarbas.objects.filter(naudotojas=self.request.user)

class PridetiDarbaView(LoginRequiredMixin, FormView):
    form_class = DarboForm
    template_name = "darzas/naujas_darbas.html"
    success_url = "/augalai/succes/"
    def form_valid(self, form):
        form.instance.naudotojas=self.request.user
        form.save()
        return super().form_valid(form)
    def get_queryset(self):
        return DarzoDarbas.objects.filter(naudotojas=self.request.user)

@login_required
def darbo_redagavimas(request, pk):
    darzodarbas = DarzoDarbas.objects.get(pk=pk)
    if request.method == 'POST':
        form = DarboForm(request.POST, instance=darzodarbas)
        if form.is_valid():
            form.save()
    else:
        form = DarboForm(instance=darzodarbas)
    return render(request, 'darzas/darbo_redagavimas.html', {'form': form})

@login_required
def darbo_pasalinimas(request, pk):
    darzodarbas = get_object_or_404(DarzoDarbas, pk=pk)
    if request.method == 'POST':
        darzodarbas.delete()
        return redirect("darbai")




class DarzoPrieziuraListView(LoginRequiredMixin, ListView):
    model = DarzoPrieziura
    template_name = "darzas/darzo_prieziura_list.html"
    context_object_name = "darzo_prieziura"
    paginate_by = 3
    def get_queryset(self):
        return DarzoPrieziura.objects.filter(darzas__augalas__naudotojas=self.request.user)

class DarzoPrieziuraDetailView(LoginRequiredMixin, DetailView):
    model = DarzoPrieziura
    template_name = "darzas/darzo_prieziura_detail.html"
    def get_queryset(self):
        return DarzoPrieziura.objects.filter(darzas__augalas__naudotojas=self.request.user)

class NaujaPrieziuiraView(LoginRequiredMixin, FormView):
    form_class = DarzoPriuziurosForm
    template_name = "darzas/nauja_prieziura.html"
    success_url = "/augalai/succes/"
    def form_valid(self, form):
        form.instance.naudotojas=self.request.user
        form.save()
        return super().form_valid(form)
    def get_queryset(self):
        return DarzoPrieziura.objects.filter(darzas__augalas__naudotojas=self.request.user)

@login_required
def prieziuros_redagavimas(request, pk):
    darzoprieziura = DarzoPrieziura.objects.get(pk=pk)
    if request.method == 'POST':
        form = DarzoPriuziurosForm(request.POST, instance=darzoprieziura)
        if form.is_valid():
            form.save()
    else:
        form = DarzoPriuziurosForm(instance=darzoprieziura)
    return render(request, 'darzas/darzo_prieziura_redagavimas.html', {'form': form})

@login_required
def darzo_prieziuros_pasalinimas(request, pk):
    darzoprieziura = get_object_or_404(DarzoPrieziura, pk=pk)
    if request.method == 'POST':
        darzoprieziura.delete()
        return redirect("darzo_darbai")




class DarzoDerliusListView(LoginRequiredMixin, ListView):
    model = DarzoDerlius
    template_name = "darzas/darzo_derlius_list.html"
    context_object_name = "derlius"
    paginate_by = 3
    def get_queryset(self):
        return DarzoDerlius.objects.filter(augalas__naudotojas=self.request.user)

class DarzoDerliusDetailView(LoginRequiredMixin, DetailView):
    model = DarzoDerlius
    template_name = "darzas/darzo_derlius_detail.html"
    def get_queryset(self):
        return DarzoDerlius.objects.filter(augalas__naudotojas=self.request.user)


class AugaluDerliusView(LoginRequiredMixin, FormView):
    form_class = DarzoDerliausForm
    template_name = "darzas/naujas_derlius.html"
    success_url = "/augalai/succes/"
    def form_valid(self, form):
        form.instance.naudotojas=self.request.user
        form.save()
        return super().form_valid(form)
    def get_queryset(self):
        return DarzoDerlius.objects.filter(augalas__naudotojas=self.request.user)

@login_required
def derliaus_redagavimas(request, pk):
    darzoderlius = DarzoDerlius.objects.get(pk=pk)
    if request.method == 'POST':
        form = DarzoDerliausForm(request.POST, instance=darzoderlius)
        if form.is_valid():
            form.save()
    else:
        form = DarzoDerliausForm(instance=darzoderlius)
    return render(request, 'darzas/darzo_derliaus_redagavimas.html', {'form': form})

@login_required
def darzo_derliaus_pasalinimas(request, pk):
    darzoderlius = get_object_or_404(DarzoDerlius, pk=pk)
    if request.method == 'POST':
        darzoderlius.delete()
        return redirect("derlius")
