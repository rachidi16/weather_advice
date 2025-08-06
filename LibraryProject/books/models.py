from django.db import models

class User(models.Model):
    pass

class Profile(models.Model):
    user = models.OneToOneField(on_delete=models.CASCADE)
