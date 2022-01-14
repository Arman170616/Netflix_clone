from distutils.command.upload import upload
from venv import create
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

MOVIE_CHOICES = (
    ('Seasonal','Seasonal'),
    ('Single', 'Single')
)


class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile',  blank = True)


class Profile(models.Model):
    name = models.CharField(max_length=225)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True, null=True)
    created_by = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    movie_type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    video = models.ManyToManyField('video')
    flyer = models.ImageField(upload_to='flyers')
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)

class Video(models.Model):
    title = models.CharField(max_length=225, blank=True, null=True)
    files=models.FileField(upload_to='movies')





