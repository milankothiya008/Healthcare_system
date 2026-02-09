from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import PatientProfile


@login_required
def patient_home(request):
    return render(request, "patients/patient_home.html")


@login_required
def patient_profile(request):
    profile, created = PatientProfile.objects.get_or_create(
        user=request.user
    )
    return render(
        request,
        "patients/patient_profile.html",
        {"profile": profile}
    )
