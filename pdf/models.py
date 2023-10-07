from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=25)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    skill = models.TextField()
    about_you = models.TextField()
    previous_work = models.TextField()