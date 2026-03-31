from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='customer_photos/', null=True, blank=True)
    note = models.TextField(blank=True)
    received_date = models.DateField(null=True, blank=True)
    delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Blouse(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blouse_images/', null=True, blank=True)
