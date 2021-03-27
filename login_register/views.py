from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm, RegistrationForm
from .models import User
import bcrypt

def login_view(request):
    return render(request, 'login_view.html', {'LoginForm': LoginForm})

def register_view(request):
    return render(request, 'register_view.html', {'RegistrationForm': RegistrationForm})

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if errors:
            for err, val in errors.items():
                messages.error(request, val)
            return redirect("/")

        user = User.objects.get(email=request.POST['email'])

        userObj = {
            "user_id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }

        request.session['user'] = userObj

        return redirect("/selectplayer")
    

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)

        if errors:
            for err, val in errors.items():
                messages.error(request, val)
            return redirect("/registration")

        hashed_password = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt()).decode('utf-8')

        new_user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=hashed_password, birthday=request.POST["birthday"])

        new_user.save()

        userObj = {
            "user_id": new_user.id,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
        }

        request.session['user'] = userObj
        
        return redirect("/selectplayer")
