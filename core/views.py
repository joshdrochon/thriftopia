from django.shortcuts import render, redirect

def logout(request):
    request.session.flush()
    return redirect("/")
