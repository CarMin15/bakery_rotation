from datetime import datetime

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

    @property
    def timesince(self, default="just now"):
        """
        Returns string representing "time since" e.g.
        3 days ago, 5 hours ago etc.
        """
        now = datetime.utcnow()
        diff = now - datetime(
            self.date.year, self.date.month, self.date.day
        )

        periods = (
            (diff.days // 365, "year", "years"),
            (diff.days // 30, "month", "months"),
            (diff.days // 7, "week", "weeks"),
            (diff.days, "day", "days"),
            (diff.seconds // 3600, "hour", "hours"),
            (diff.seconds // 60, "minute", "minutes"),
            (diff.seconds, "second", "seconds"),
        )

        for period, singular, plural in periods:
            if period:
                return "%d %s ago" % (
                    period, singular if period == 1 else plural
                )

        return default
