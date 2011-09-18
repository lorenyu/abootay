from django.shortcuts import render_to_response
from game.models import Card

def index(request):
    return render_to_response('index.html')

def cards(request):
    cards = Card.objects.all()
    return render_to_response('cards/index.html', {'cards' : cards})
