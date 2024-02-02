from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    message = models.TextField(max_length=1000)



# Create your models here.
