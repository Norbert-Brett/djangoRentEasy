from django.db import models
from datetime import datetime

from hosts.models import Host
from listings.validators import allow_only_images_validator


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
    photo_main = models.ImageField(upload_to='photos/listings/',validators=[allow_only_images_validator])
    date_from = models.DateField(default=datetime.now, blank=True)
    date_to = models.DateField(default=datetime.now, blank=True)
    photo_1 = models.ImageField(upload_to='photos/listings/', blank=True, validators=[allow_only_images_validator])
    photo_2 = models.ImageField(upload_to='photos/listings/', blank=True, validators=[allow_only_images_validator])
    photo_3 = models.ImageField(upload_to='photos/listings/', blank=True, validators=[allow_only_images_validator])
    photo_4 = models.ImageField(upload_to='photos/listings/', blank=True, validators=[allow_only_images_validator])
    photo_5 = models.ImageField(upload_to='photos/listings/', blank=True, validators=[allow_only_images_validator])
    photo_6 = models.ImageField(upload_to='photos/listings/', blank=True, validators=[allow_only_images_validator])
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
