from django.db import models


class Hero(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    superpower = models.TextField(default="")
