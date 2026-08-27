from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

PROFILE_PIC_PATH = 'users/profile_pic'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=PROFILE_PIC_PATH)
    birth_date = models.DateField(null=True, blank=True)

