from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    vat_id = models.CharField(max_length=11)
    street = models.TextField()
    city = models.TextField()
    country = models.TextField()

    def __str__(self):
        return self.name
    