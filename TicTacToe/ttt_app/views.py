from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Game

# Create your views here.

def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        option = request.POST.get("option")
        room_code = request.POST.get("room_code")

        if option == '1':
            game = Game.objects.filter(room_code = room_code).first()

            if game is None:
                messages.info(request, "Room not found")
                return redirect('/')
            
            if game.isOver:
                messages.info(request, 'Game is over')
                return redirect('/')
            
            game.opponent = username
            game.save()
            
        
        else:
            game = Game(room_creater = username, room_code=room_code)
            game.save()

            return redirect("/play/"+room_code+'?username='+username)

    return render(request, 'home.html')

def game(request, room_code):
    username = request.GET.get('username')
    context = {'room_code':room_code, 'username':username}
    return render(request, 'tictactoe.html', context=context)