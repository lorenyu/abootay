from django.db import models

class Card(models.Model):
    phrase = models.CharField(max_length=256)
