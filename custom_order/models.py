from django.db import models
from products.models import Category
from profiles.models import UserProfile
from django.core.exceptions import ValidationError


MATERIALS = ((0, 'Polymer Clay'), (1, 'Gemstones and Crystals'), (2, 'Wire'),
             (3, 'Beads'))


class CustomOrder(models.Model):
    """
    CustomOrder model
    """
    category = models.ForeignKey(Category, null=False, blank=False,
                                 on_delete=models.CASCADE)
    material = models.IntegerField(choices=MATERIALS, blank=False)
    product_id = models.IntegerField(blank=False, default=1000)
    product_name = models.CharField(max_length=80, blank=False,
                                    default='Your Custom Order')
    colour_scheme = models.CharField(max_length=80, blank=False)
    charm = models.BooleanField(default=False, blank=False)
    personalised = models.BooleanField(default=False, blank=False)
    name = models.CharField(max_length=80, blank=True)
    additional_details = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    MATERIAL_PRICES = {
        0: 8.00,
        1: 14.00,
        2: 10.00,
        3: 8.00,
        }

    def clean(self):
        """
        Overrides the clean method to add form validation.
        If customer chooses personalised they must supply
        a name in the name field.
        """
        super().clean()
        if self.personalised and not self.name:
            raise ValidationError({'name': 'A name is required for '
                                  'personalised items.'})

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the price. price is determined
        on the choice of material. If a customer chooses to add a charm it will
        add 2.50. If personalised is chosen it adds 2.50 to the price.
        """

        material_price = self.MATERIAL_PRICES.get(self.material, 0)

        if self.charm:
            material_price += 2.50

        if self.personalised:
            material_price += 2.50

        self.price = material_price

        super().save(*args, **kwargs)
