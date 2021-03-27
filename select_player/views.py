import os
from django.shortcuts import render, redirect
from .models import User, Class, Player


def select_player_view(request):
    
    user = User.objects.filter(id=request.session['user']['user_id'])

    if user:
        [user] = user

        user_players = user.players.all()

        new_player_cards = []

        for i in range(3 - len(user.players.all())):
            new_player_cards.append(i)

        view_data = {
            'user_players': user_players,
            'new_player_cards': new_player_cards,
        }

        if user_players:
            return render(request, 'select_player_view.html', view_data)
        else:
            return redirect('/newplayer')

def new_player_view(request):
    player_classes = Class.objects.all()

    return render(request, 'new_player_view.html', {'player_classes': player_classes,})

def assign_player(request, class_id):
    if request.method == "POST":
        user = User.objects.get(id=request.session['user']['user_id'])
        selected_class = Class.objects.get(id=class_id)

        print("SCLASS:", selected_class.name)
        new_player = Player.objects.create(p_class=selected_class, user=user)
        request.session['player_id'] = new_player.id

        return redirect('/thriftopia')

def select_player(request, player_id):
    request.session['player_id'] = player_id
    return redirect('/thriftopia')

        
