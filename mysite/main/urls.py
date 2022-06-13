from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("wiki/", views.wiki, name="wiki"),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout_request, name="logout"),
    path("password_reset/", views.password_reset_request, name="password_reset"),
    path("apteki/", views.apteki, name="apteki"),
    path("printers/", views.printers, name="printers"),
    path("equipment/", views.equipmentview, name='equipment'),
    path("equipment_list/", views.list_apteka_equipment, name='equipment_list'),
    path("lan_list/", views.list_apteka_lan, name='lan_list'),
]