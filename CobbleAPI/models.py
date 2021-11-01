from django.db import models
from django.contrib.auth.models import User


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    wallet = models.CharField(max_length=42)
    mcusername = models.CharField(max_length=20, unique=True)
    mcsecret = models.CharField(max_length=150)
    validated = models.BooleanField()

    cobbleCoinHold = models.FloatField(default=0)

    coalHold = models.FloatField(default=0)
    ironHold = models.FloatField(default=0)
    goldHold = models.FloatField(default=0)
    diamondHold = models.FloatField(default=0)

    def __str__(self):
        return self.username


class Exchange(models.Model):
    name = models.CharField(max_length=150, unique=True)
    registeree = models.CharField(max_length=20)
    exFee = models.IntegerField(default=0)

    coalSignOwner = models.CharField(max_length=20, default="")
    coalSignFee = models.IntegerField(default=0)
    coalSignSet = models.BooleanField(default=False)
    coalSignLocationWorld = models.CharField(max_length=260, default="")
    coalSignLocationX = models.IntegerField(default=0)
    coalSignLocationY = models.IntegerField(default=0)
    coalSignLocationZ = models.IntegerField(default=0)

    ironSignOwner = models.CharField(max_length=20, default="")
    ironSignFee = models.IntegerField(default=0)
    ironSignSet = models.BooleanField(default=False)
    ironSignLocationWorld = models.CharField(max_length=260, default="")
    ironSignLocationX = models.IntegerField(default=0)
    ironSignLocationY = models.IntegerField(default=0)
    ironSignLocationZ = models.IntegerField(default=0)

    goldSignOwner = models.CharField(max_length=20, default="")
    goldSignFee = models.IntegerField(default=0)
    goldSignSet = models.BooleanField(default=False)
    goldSignLocationWorld = models.CharField(max_length=260, default="")
    goldSignLocationX = models.IntegerField(default=0)
    goldSignLocationY = models.IntegerField(default=0)
    goldSignLocationZ = models.IntegerField(default=0)

    diamondSignOwner = models.CharField(max_length=20, default="")
    diamondSignFee = models.IntegerField(default=0)
    diamondSignSet = models.BooleanField(default=False)
    diamondSignLocationWorld = models.CharField(max_length=260, default="")
    diamondSignLocationX = models.IntegerField(default=0)
    diamondSignLocationY = models.IntegerField(default=0)
    diamondSignLocationZ = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
