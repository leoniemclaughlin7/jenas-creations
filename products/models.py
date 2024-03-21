from django.db import models


class Category(models.Model):
    """
    Category model
    """

    class Meta:
        """
        Adds the plural of category, categories.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        """
        Returns the category name.
        """
        return self.name


class Product(models.Model):
    """
    Product model
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=False)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        """
        Returns product name
        """
        return self.name
