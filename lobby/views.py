from django.shortcuts import render, redirect

# Create your views here.

def lobby(request, lobby_id):
    if request.method=="POST":
        if "comenzar" in request.POST:
            return redirect("bingo")

    return render(request, "lobby.html",{
        'lobby_id':lobby_id
        })