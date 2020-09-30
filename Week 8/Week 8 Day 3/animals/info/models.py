from django.db import models

# Create your models here.


class Family(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"

class Animal(models.Model):
    name = models.CharField(max_length=30)
    legs = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    speed = models.IntegerField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}" 

