from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.


class WeatherData(models.Model):
    date = models.DateField()
    city = models.CharField(max_length=50)
    avg_temp = models.FloatField()
    condition = models.CharField(max_length=300)
    hourdata = JSONField()
