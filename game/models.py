from django.db import models


class Card(models.Model):
    # Card will have a field called id, which is an auto-incrementing
    # primary key
    deck = models.ForeignKey('Deck', related_name = 'cards')
    phrase = models.CharField(max_length=255)
    abootayWordOne = models.CharField(max_length=63)
    abootayWordTwo = models.CharField(max_length=63)
    abootayWordThree = models.CharField(max_length=63)
    abootayWordFour = models.CharField(max_length=63)
    abootayWordFive = models.CharField(max_length=63)
    abootayWordSix = models.CharField(max_length=63)

    @property
    def tabooWords( self ):
        return[ tabooWordOne, tabooWordTwo, tabooWordThree, tabooWordFour,
                tabooWordFive, tabooWordSix ]

class Deck( models.Model ):
    # Deck will have a field called id, which is an auto-incrementing 
    # primary key
    # Deck will also have a field called 'cards' by virtue of the ForeignKey
    # relationship with the Card class setup above
    title = models.CharField( max_length=255, unique=True )
    
