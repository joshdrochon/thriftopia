from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('login_register.urls')),
    path('', include('select_player.urls')),
    path('', include('game.urls')),
]
