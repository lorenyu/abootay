from django.shortcuts import render_to_response
from abootay.models import Card

def index(request):
    cards = Card.objects.all()
    return render_to_response('cards/index.html', {'cards' : cards})
    
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
