from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reserver/", views.reserver, name="reserver"),
    path('mes-reservations/', views.mes_reservations, name='mes_reservations'),
    path('salles/', views.liste_salles_web, name='salles'),
    path('supprimer/<int:id>/', views.supprimer_reservation, name='supprimer'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inscription/', views.inscription, name='inscription'),
    #path('admin-panel/', views.dashboard, name='dashboard'),
    path('annuler/<int:reservation_id>/', views.annuler_reservation, name='annuler'),
    path("admin-salles/", views.admin_salles, name="admin_salles"),
    path("admin-reservations/", views.admin_reservations, name="admin_reservations"),
    path("admin-users/", views.admin_users, name="admin_users"),
    path('admin-annuler/<int:id>/', views.admin_annuler, name='admin_annuler'),


]


