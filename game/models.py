from django.db import models

class Card(models.Model):
    phrase = models.CharField(max_length=256,primary_key=True)
    tabooWordOne = models.CharField(max_length=64)
    tabooWordTwo = models.CharField(max_length=64)
    tabooWordThree = models.CharField(max_length=64)
    tabooWordFour = models.CharField(max_length=64)
    difficultyLevel = models.IntegerField(null=True)

    @property
    def tabooWords( self ):
        return[ tabooWordOne, tabooWordTwo, tabooWordThree, tabooWordFour ]
