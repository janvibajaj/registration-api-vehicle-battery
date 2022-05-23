from django.db import models

# Create your models here.
class RegistrationList(models.Model):
    name = models.CharField(max_length=70)
    number = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.TextField()
    number_plate = models.CharField(max_length=20)
    type_of_vehicle = models.CharField(max_length=50)
    date = models.DateField()
    
    def __str__(self):
        return self.name
  
  
