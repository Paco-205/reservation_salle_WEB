from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("reserver/", views.reserver, name="reserver"),
    path('mes-reservations/', views.mes_reservations, name='mes_reservations'),
    path('annuler/<int:reservation_id>/', views.annuler_reservation, name='annuler'),
    
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('inscription/', views.inscription, name='inscription'),
    
    # Admin
    path('admin-panel/', views.dashboard, name='dashboard'),
    path('admin-annuler/<int:id>/', views.admin_annuler, name='admin_annuler'),
    path('admin-creer-salle/', views.admin_creer_salle, name='admin_creer_salle'),
    path('admin-modifier-salle/<int:id>/', views.admin_modifier_salle, name='admin_modifier_salle'),
    path('admin-supprimer-salle/<int:id>/', views.admin_supprimer_salle, name='admin_supprimer_salle'),
    path("admin-users/", views.admin_users, name="admin_users"),
]