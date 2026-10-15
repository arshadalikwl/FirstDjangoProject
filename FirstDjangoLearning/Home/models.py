from django.db import models

# Create your models here.
class Contact(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.CharField(max_length=254)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    date    = models.DateTimeField(auto_now_add=True) 
