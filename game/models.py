from django.db import models

class Card(models.Model):
    phrase = models.CharField(max_length=256,primary_key=True)
    abootayWordOne = models.CharField(max_length=64)
    abootayWordTwo = models.CharField(max_length=64)
    abootayWordThree = models.CharField(max_length=64)
    abootayWordFour = models.CharField(max_length=64)
    difficultyLevel = models.IntegerField(null=True)

    @property
    def tabooWords( self ):
        return[ tabooWordOne, tabooWordTwo, tabooWordThree, tabooWordFour ]
