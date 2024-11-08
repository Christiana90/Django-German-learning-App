# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from .models import Register


def home(request):
    return render(request, 'registration/home.html')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            # Retrieve the password fields
            password = form.cleaned_data.get("password")
            confirm_password = form.cleaned_data.get("confirm_password")
            
            # Check if passwords match
            if password == confirm_password:
                # Save user data to the database (excludes confirm_password)
                form.save()
                
                # Display a success message and redirect to a success page or login page
                return ("<html>Registration successful! Please log in.</html>")
                #return redirect("login")  # Replace with the actual URL name for login or success
            else:
                form.add_error("confirm_password", "Passwords do not match")
    else:
        form = RegisterForm()
    
    return render(request, "registration/register.html", {"form": form})