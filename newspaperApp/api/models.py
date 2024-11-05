from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Authors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comments(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now=True)

    
        

