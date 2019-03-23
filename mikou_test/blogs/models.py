from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.content


class HashTag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    message = models.ManyToManyField(Message)

    def __str__(self):
        return self.name
