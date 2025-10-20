from django.shortcuts import render

# Create your views here.

def juego(request):
    return render(request, "juego.html")