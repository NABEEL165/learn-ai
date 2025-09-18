from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
# Admin Login View
def adminlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_superuser:  # ✅ Only superusers
            login(request, user)
            messages.success(request, f"Welcome Admin {username} 🚀")
            return redirect("/")  # Change to your dashboard URL
        else:
            messages.error(request, "❌ Invalid credentials or not an admin!")
            return redirect("adminlogin")

    return render(request, "adminlogin.html")  # Your custom template



def adminprofile(request):
    return render(request, "adminprofile.html")