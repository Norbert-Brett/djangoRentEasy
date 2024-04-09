from django.db import models
from datetime import datetime

from hosts.models import Host


class Listing(models.Model):
    host = models.ForeignKey(Host, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField(default=1)
    bathrooms = models.IntegerField(default=1)
    guests = models.IntegerField(default=1)
    photo_main = models.ImageField(upload_to='photos/listings/')
    date_from = models.DateField(default=datetime.now, blank=True)
    date_to = models.DateField(default=datetime.now, blank=True)
    photo_1 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/listings/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/listings/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
