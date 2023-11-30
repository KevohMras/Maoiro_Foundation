from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    Email = models.CharField(max_length=25)
    Message = models.TextField()


class Subscribe(models.Model):
    email = models.EmailField(max_length=20)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name