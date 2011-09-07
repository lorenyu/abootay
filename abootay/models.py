from django.db import models
import datetime

class Card(models.Model):
    phrase = models.CharField(max_length=256)
