from django.db import models

# Create your models here.
class Master(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)