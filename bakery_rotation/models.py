from django.db import models

# Create your models here.

class BakingSlot(models.Model):
    item = models.CharField(max_length=200)
    date = models.DateField()
