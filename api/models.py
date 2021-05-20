from django.db import models

# Create your models here.
class Business(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    owner_info = models.CharField(max_length=150)
    employee_size = models.IntegerField()
    
    def __str__(self):
        return self.name