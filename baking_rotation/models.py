from datetime import datetime

import pytz

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
    description = models.TextField(max_length=400, default='')

    def __str__(self):
        return 'BakingSlot: {}, {}'.format(self.date, self.item)

    class Meta:
        ordering = ['date']

    @staticmethod
    def period_name(diff):
        return (
            (diff.days // 365, "year", "years"),
            (diff.days // 30, "month", "months"),
            (diff.days // 7, "week", "weeks"),
            (diff.days, "day", "days"),
        )

    @property
    def pretty_time(self):
        if self.date >= datetime.utcnow().date():
            return self.timeuntil
        else:
            return self.timesince

    @property
    def timesince(self, default="just now"):
        """
        Returns string representing "time since" e.g.
        3 days ago, yesterday, etc.
        """
        now = datetime.now(pytz.timezone('America/New_York'))
        dt = datetime(
            self.date.year, self.date.month, self.date.day,
            tzinfo=pytz.timezone('America/New_York')
        )
        if dt.day == now.day:
            return 'today'
        elif now.day - dt.day == 1:
            return 'yesterday'
        else:
            diff = now - dt
            for period, singular, plural in self.period_name(diff):
                if period:
                    return "%d %s ago" % (
                        period, singular if period == 1 else plural
                    )
            return 'soon'


    @property
    def timeuntil(self):
        """
        Returns string representing "time until" e.g.
        in 3 days, tomorrow, etc.
        """
        now = datetime.now(pytz.timezone('America/New_York'))
        dt = datetime(
            self.date.year, self.date.month, self.date.day,
            tzinfo=pytz.timezone('America/New_York')
        )
        if dt.day == now.day:
            return 'today'
        elif dt.day - now.day == 1:
            return 'tomorrow'
        else:
            diff = dt - now
            for period, singular, plural in self.period_name(diff):
                if period:
                    return "in %d %s" % (
                        period, singular if period == 1 else plural
                    )
            return 'soon'
