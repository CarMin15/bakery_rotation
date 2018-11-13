from django.db import models
from django.contrib.auth.models import User


class BakingSlot(models.Model):
    item = models.CharField(max_length=200)
    date = models.DateField(unique=True)
    baker = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='slots'
    )
    image = models.ImageField(
        upload_to='uploads/baking_slot_images/%Y/%m/%d/',
        null=True
    )

    def __str__(self):
        return 'BakingSlot: {}, {}'.format(self.date, self.item)

    class Meta:
        ordering = ['date']
