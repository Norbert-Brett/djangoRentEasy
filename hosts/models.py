from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Host(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='host_profile')
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/hosts/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    host_since = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
