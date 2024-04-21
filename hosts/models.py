from django.db import models
from datetime import datetime


class Host(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/hosts/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    host_since = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name