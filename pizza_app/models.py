from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_type=models.CharField(max_length=50,default=None)
    pizza_size=models.CharField(max_length=50,default=None)
    toppings=models.CharField(max_length=100,default=None)

    def __str__(self):
        return self.pizza_type