from django.urls import path
from .views import game_view, process_destination, get_experience

urlpatterns = [
    path('thriftopia', game_view),
    path('process_destination/<str:destination>', process_destination, name="proc_destination"),
    path('get_experience', get_experience),
]