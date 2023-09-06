from django.db import models

# Create your models here.

class Mobile(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    