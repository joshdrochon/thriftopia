from django.shortcuts import render, HttpResponse
import json
import random
from django.core import serializers
from select_player.models import User,Player, Item, Class

destinations = [
    "Thrift Store", "Casino", "Mom & Dads", "Home", "Record Store", "Coffee Shop", "Farmer's Market", "Grocery Store", "Pizza Town", "Take a Walk", "Garage Sale", "Lumber Yard", "Auction", "Last Byte", "Tech Repair Shop", "It's About Thyme", "Estate Sale", "Web Search", "Tailor Service"
]

def game_view(request):
    if not "activities" in request.session:
        request.session['activities'] = []

    player = Player.objects.get(id=request.session['player_id'])

    p_class = Class.objects.get(id=player.p_class_id)

    view_data = {
        "player": player,
        "p_class": p_class,
        "destinations": destinations,
    }

    return render(request, 'game_view.html', view_data)

def add_experience(request, xp):
    if not 'experience' in request.session:
        request.session['experience'] = 0
    request.session['experience'] += xp

def get_experience(request):
    xp = 0
    if not 'experience' in request.session:
        xp = 3
    else:
        xp = request.session['experience'] + 3
    return HttpResponse(json.dumps(xp), status=200)

def process_destination(request, destination):
    if request.method == "POST":
        random_int = random.randint(0, len(Item.objects.all()) - 1)
        item = Item.objects.all()[random_int]
        message = f"Found {item.name} at {destination}"
        message = {"message": message}
        sessionlist = request.session['activities']
        sessionlist.append(message)
        request.session['activities'] = sessionlist

        add_experience(request, 3)

        return HttpResponse(json.dumps(sessionlist), status=200)
