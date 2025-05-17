from django.urls import path
from . import views

app_name = "rental"

urlpatterns = [path("reservations/", views.reservations, name="reservations")]
