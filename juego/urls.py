"""URLS JUEGO"""
from django.urls import path
from .views import juego_trivia

urlpatterns = [
    path('', juego_trivia, name='juego'),
    #path('logout',user_logout ,name='user_logout'),
]
