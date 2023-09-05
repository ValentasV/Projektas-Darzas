from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from vartotojai.models import Vartotojas


# Create your views here.

class VartotojoRegistracijaView(View):
    def get(self, request):
        return render(request, "registracija/registracija.html")

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            Vartotojas.objects.get(email=email)
            return render(request, "registracija/registracija.html",
                          {"klaida": "Vartotojas su tokiu elektroniniu paštu jau egzistuoja"})
        except Vartotojas.DoesNotExist:
            pass

        vartotojas = Vartotojas(first_name=first_name, last_name=last_name, phone=phone, email=email)
        vartotojas.set_password(password)
        vartotojas.save()
        return redirect(reverse("prisijungimo_forma"))



class VartotojoPrisijungimoView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "vartotojai/prisijungimas.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("username")
            print("EMAIL", email)
            password = form.cleaned_data.get("password")
            user = Vartotojas.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect("/vartotojai/pasisveikinimas")
            else:
                form.add_error(None, "Neteisingas slaptažodis")
        return render(request, "vartotojai/prisijungimas.html", {"form": form})

@login_required
def pasisveikinimas_view(request):
    return render(request, "vartotojai/pasisveikinimas.html")



class VartotojoAtsijungimasView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("prisijungimo_forma")


class VartotojoIstrynimasView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "vartotojai/istrynimas.html")

    def post(self, request):
        user = request.user  # Get the currently logged-in user
        # Delete the user
        user.delete()
        # Redirect to a confirmation page or anywhere you prefer
        return redirect(reverse("confirmation_page"))

