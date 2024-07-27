from django.db import models

# Create your models here.
class stock_data(models.Model):
    name=models.CharField(max_length=100)
    oc_diff=models.CharField(max_length=100)
    volume=models.CharField(max_length=100)
    indicater=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name