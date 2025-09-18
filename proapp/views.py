from django.shortcuts import render

# Create your views here.







def index(request):
    return render(request, 'index.html')

def ai(request):
    return render(request, 'ai.html')

def mechine(request):
    return render(request, 'mechine.html')
def deep(request):
    return render(request, 'deep.html')





from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Check passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match ❌")
            return redirect("register")

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken ❌")
            return redirect("login")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered ❌")
            return redirect("register")

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        # Auto login after registration
        login(request, user)
        messages.success(request, "Registration successful 🎉")
        return redirect("login")  # change 'home' to your home page url name

    return render(request, "register.html")




from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome {username}, you are now logged in!")
            return redirect("/")  # Change "home" to your home page url name
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, "login.html")





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
            return redirect("adminprofile")  # Change to your dashboard URL
        else:
            messages.error(request, "❌ Invalid credentials or not an admin!")
            return redirect("adminprofile")

    return render(request, "admin/adminlogin.html")  # Your custom template








def expert_view(request):
    return render(request, "expert.html")




from django.shortcuts import render, redirect
from .models import Contact

def save_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Contact.objects.create(name=name, email=email, message=message)
        return redirect("/")  # Redirect to table page
    return redirect("contact")

def contact_list(request):
    contacts = Contact.objects.all().order_by("-created_at")
    return render(request, "contact_list.html", {"contacts": contacts})


def adminprofile(request):
    return render(request, "admin/adminprofile.html")




from django.contrib.auth.models import User
from django.shortcuts import render

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})




def aiprojeect(request):
    return render(request, 'aiproject.html')



def guidence(request):
    return render(request, 'guidence.html')