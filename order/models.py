from django.db import models

class Product(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class ProductOrderPosition(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        related_name='positions',
    )
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    comment = models.TextField()
    products = models.ManyToManyField(
        Product,
        through=ProductOrderPosition,
    )
