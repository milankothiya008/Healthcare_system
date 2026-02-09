from django.urls import path
from .views import patient_home, patient_profile

urlpatterns = [
    path("patient/home/", patient_home, name="patient_home"),
    path("patient/profile/", patient_profile, name="patient_profile"),
]
