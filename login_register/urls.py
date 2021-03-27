from django.urls import path
from .views import login_view, register_view, login, register

urlpatterns = [
    path('', login_view),
    path('login', login),
    path('register', register),
    path('registration', register_view)
]