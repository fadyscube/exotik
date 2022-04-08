from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    done = models.BooleanField(default=False)
    date = models.CharField(max_length=10, default=str(datetime.date(datetime.now())))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_random = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    @classmethod
    def get_dates(self):
        dates = []
        for i in self.objects.all():
            if i.date not in dates:
                dates.append(i.date)

        return dates