from django.db import models


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    message = models.CharField(max_length=255)
    

