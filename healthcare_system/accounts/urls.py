from django.urls import path
from .views import register_choice, patient_register, login_page, logout_view

urlpatterns = [
    path("", register_choice, name="register_choice"),
    path("register/patient/", patient_register, name="patient_register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_view, name="logout"),
]
