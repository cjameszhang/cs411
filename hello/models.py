from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=64)
    last_update = models.DateTimeField()
    score = models.IntegerField()
    image = models.FileField(upload_to='.')
    imgurl = models.CharField(max_length=16)

class Vote(models.Model):
    voter = models.CharField(max_length=64)
    votee = models.CharField(max_length=64)
    last_update = models.IntegerField()
    direction = models.IntegerField()
