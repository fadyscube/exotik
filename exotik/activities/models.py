from django.db import models

# Create your models here.

class Activity(models.Model):
    activity = models.CharField(max_length=255)
    _type = models.CharField(max_length=255)

    def __str__(self):
        return self.activity

    class Meta:
        verbose_name_plural = "activities"
