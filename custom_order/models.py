from django.db import models
from products.models import Category

MATERIALS = ((0, 'Polymer Clay'), (1, 'Gemstones and Crystals'), (2, 'Wire'), (3, 'Beads'))

class CustomOrder(models.Model):
    category = models.ForeignKey(Category, null=False, blank=False, on_delete=models.CASCADE)
    material = models.PositiveIntegerField(choices=MATERIALS)
    colour_scheme = models.CharField(max_length=80, blank=False)
    charm = models.BooleanField(default=False, blank=False)
    personalised =  models.BooleanField(default=False, blank=False)
    name = models.CharField(max_length=80, blank=True) 
    additional_details = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)


    def clean(self):
        super.clean()
        if self.personalised and not self.name:
            raise ValidationError({'A name is required for personalised items.'})


    def save(self, *args, **kwargs):
        """
        Override the original save method to set the price.
        """
        MATERIAL_PRICE = {
        0: 8.00,
        1: 14.00,
        2: 10.00,
        3: 8.00,
        }
        
        material_price = self.MATERIAL_PRICES.get(self.material, 0)

        if self.charm:
            material_price += 2.50

        if self.personalised:
            material_price += 2.50

        self.price = material_price
        
        super().save(*args, **kwargs)