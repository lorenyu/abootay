from django.shortcuts import render_to_response
from game.models import Card, Deck
from django.core import serializers

def play(request):
    cards = Card.objects.all()
    cardsjson = serializers.get_serializer("json")().serialize( cards, ensure_ascii=False )
    return render_to_response('play.html', { 'cardsjson' : cardsjson } )

def index(request):
    return render_to_response('index.html')

def cards(request):
    cards = Card.objects.all()
    return render_to_response('cards/index.html', {'cards' : cards})
