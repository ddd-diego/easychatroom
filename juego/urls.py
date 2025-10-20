from django.urls import path
from .views import juego

urlpatterns = [
    path('bingo/', juego, name="bingo"),
]