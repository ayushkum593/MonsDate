from django.db import models
from django import models

class Profile(models.Model):
    user_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    bio = models.TextField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

