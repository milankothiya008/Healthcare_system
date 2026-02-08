from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def register_choice(request):
    return render(request, "accounts/register_choice.html")


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()


def patient_register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            return render(
                request,
                "accounts/patient_register.html",
                {"error": "Passwords do not match"}
            )

        if User.objects.filter(email=email).exists():
            return render(
                request,
                "accounts/patient_register.html",
                {"error": "Email already registered"}
            )

        User.objects.create_user(
            email=email,
            password=password,
            phone=phone,
            role="PATIENT",
            status="APPROVED"
        )

        return redirect("/login/")

    return render(request, "accounts/patient_register.html")
def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)

        if user is None:
            return render(
                request,
                "accounts/login.html",
                {"error": "Invalid email or password"}
            )

        # Check approval status
        if user.status != "APPROVED":
            return render(
                request,
                "accounts/login.html",
                {"error": "Your account is not approved yet"}
            )

        # Login user
        login(request, user)

        # Role-based redirect
        if user.role == "PATIENT":
            return redirect("/patient/home/")
        elif user.role == "DOCTOR":
            return redirect("/doctor/dashboard/")
        elif user.role == "HOSPITAL_ADMIN":
            return redirect("/hospital/dashboard/")
        elif user.role == "SYSTEM_ADMIN":
            return redirect("/system-admin/dashboard/")
        else:
            return render(
                request,
                "accounts/login.html",
                {"error": "Invalid user role"}
            )

    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("/login/")