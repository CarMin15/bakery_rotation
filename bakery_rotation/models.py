from django.db import models

# Create your models here.

class BakingSlot(models.Model):
    item = models.CharField(max_length=200)
    date = models.DateField(unique=True)
    # img = models.ImageField()


    def __str__(self):
        return 'BakingSlot: {}, {}'.format(self.date, self.item)


    class Meta:
        ordering = ['date']
