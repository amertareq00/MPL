from django.db import models

# Create your models here.

from django.db import models

class ClientType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Food', 'Food'),
        ('Snacks', 'Snacks'),
        ('Drinks', 'Drinks'),
        ('Hardware', 'Hardware'),
    ])
    description = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} - {self.client.name}"
