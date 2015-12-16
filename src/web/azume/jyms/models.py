from django.db import models


class Jym(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_digits=21, decimal_places=18)
    lng = models.DecimalField(max_digits=21, decimal_places=18)
