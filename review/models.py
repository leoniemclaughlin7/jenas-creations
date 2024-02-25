from django.db import models
from products.models import Product


STARS = ((1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'),
        (5, '5 stars'))

class Review(models.Model):
    """
    Model for review form.
    """
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    stars = models.PositiveIntegerField(choices=STARS, default=5)
    body = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.name}"
