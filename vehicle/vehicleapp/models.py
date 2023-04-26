from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicleNumber = models.CharField(primary_key=True,max_length=25, default="")
    type  = [(2, "Two wheeler"), (3,"Three wheeler" ),(4,"Four wheeler")]
    vehicleType = models.IntegerField(default=2, choices=type)
    vehicleModel= models.CharField(max_length=25, default="")
    vehicleDescription= models.CharField(max_length=25, default="")

    def __str__(self):
        return self.vehicleNumber