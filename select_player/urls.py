from django.urls import path
from .views import select_player_view, new_player_view, assign_player, select_player

urlpatterns = [
    path('newplayer', new_player_view),
    path('selectplayer', select_player_view),
    path('assign_player/<int:class_id>', assign_player),
    path('select_player/<int:player_id>', select_player)
]