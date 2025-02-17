from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from customers.models import Customer


class Offer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # ForeignKey to Django's built-in User model
    date = models.DateField()  # Date of the offer
    sub_total = models.DecimalField(max_digits=10, decimal_places=2)  # Subtotal amount
    tax = models.DecimalField(max_digits=10, decimal_places=2)  # Tax amount
    total = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount

    items = models.ManyToManyField(Product, through='OfferItem')  # Many-to-Many relationship with Product

    def __str__(self):
        return f"Offer #{self.id} - Customer: {self.customer.username}, Total: ${self.total}"

    def save(self, *args, **kwargs):
        """
        Override save to include any custom logic before saving.
        Django automatically handles insert/update based on whether the instance has a primary key.
        """
        super().save(*args, **kwargs)

    @classmethod
    def from_tuple(cls, data):
        """
        Create an Offer instance from a tuple.
        Args:
            data (tuple): A tuple containing (id, customer_id, date, sub_total, tax, total).
        Returns:
            Offer: An instance of Offer.
        """
        return cls(
            id=data[0],
            customer_id=data[1],
            date=data[2],
            sub_total=data[3],
            tax=data[4],
            total=data[5],
        )

    @classmethod
    def get_all(cls):
        """
        Retrieve all Offer instances from the database.
        Returns:
            QuerySet: A QuerySet containing all Offer objects.
        """
        return cls.objects.all()


class OfferItem(models.Model):
    """
    Intermediate model for the Many-to-Many relationship between Offer and Product.
    This model tracks the quantity of each product in the offer.
    """
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Offer #{self.offer.id}"
