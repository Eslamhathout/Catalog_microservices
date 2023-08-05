from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=11, decimal_places=3)
    cost = models.DecimalField(max_digits=11, decimal_places=3)
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name
