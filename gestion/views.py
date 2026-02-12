from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime, date
from django.contrib import messages
from .models import Salle, Reservation
from django.utils import timezone
from django.contrib.auth.models import User



def index(request):
    salles = Salle.objects.all()
    return render(request, "gestion/index.html", {"salles": salles})


def inscription(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return render(request, "inscription.html", {"error": "Utilisateur existe déjà"})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("index")

    return render(request, "gestion/inscription.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "login.html", {"error": "Identifiants incorrects"})

    return render(request, "gestion/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")


@login_required
def liste_salles_web(request):
    salles = Salle.objects.all()
    return render(request, 'gestion/salles.html', {'salles': salles})

@login_required
def annuler_reservation(request, reservation_id):
    reservation = Reservation.objects.get(id=reservation_id)
    if reservation.user == request.user:
        reservation.delete()
    return redirect('mes_reservations')


@login_required
def mes_reservations(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, "gestion/mes_reservations.html", {"reservations": reservations})


@login_required
def reserver(request):

    salles = Salle.objects.all()

    if request.method == "POST":
        salle_id = request.POST.get("salle")
        date = request.POST.get("date")
        heure_debut = request.POST.get("heure_debut")
        heure_fin = request.POST.get("heure_fin")

        salle = Salle.objects.get(id=salle_id)

        Reservation.objects.create(
            user=request.user,
            salle=salle,
            date=date,
            heure_debut=heure_debut,
            heure_fin=heure_fin
        )

        return redirect("mes_reservations")

    return render(request, "gestion/reserver.html", {"salles": salles})


@login_required
def supprimer_reservation(request, id):
    reservation = Reservation.objects.get(id=id)

    if reservation.utilisateur == request.user:
        reservation.delete()

    return redirect("mes_reservations")

# Vue pour le dashboard admin ou il affiche le nombre de salles, de réservations et d'utilisateurs

@staff_member_required
def dashboard(request):
    nb_salles = Salle.objects.count()
    nb_reservations = Reservation.objects.count()
    nb_users = User.objects.count()

    return render(request, "gestion/admin/dashboard.html", {
        "nb_salles": nb_salles,
        "nb_reservations": nb_reservations,
        "nb_users": nb_users,
    })

def admin_required(view_func): 
    return user_passes_test(lambda u: u.is_staff)(view_func)

@admin_required
def admin_salles(request):
    salles = Salle.objects.all()
    return render(request, "gestion/admin/salles.html", {"salles": salles})

@admin_required
def admin_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, "gestion/admin/reservations.html", {
        "reservations": reservations
    })


@admin_required
def admin_users(request):
    users = User.objects.all()
    return render(request, "gestion/admin/users.html", {
        "users": users
    })
