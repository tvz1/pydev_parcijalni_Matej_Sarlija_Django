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
    
    def save(self, *args, **kwargs):
        """
        Overrides the save method to include any custom logic.
        Django automatically handles insert/update based on whether the instance has a primary key.
        """
        super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):
        """
        Creates a Product instance from a tuple.
        Args:
            data (tuple): A tuple containing (id, name, description, price).
        Returns:
            Product: An instance of Product.
        """
        return cls(id=data[0], name=data[1], description=data[2], price=data[3])

    @classmethod
    def get_all(cls):
        """
        Retrieves all Product instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Product objects.
        """
        return cls.objects.all()
