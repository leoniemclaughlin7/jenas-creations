from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=80, blank=False, null=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(blank=False, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns enquiry by: full_name.
        """
        return f'Enquiry by: {self.full_name}'
