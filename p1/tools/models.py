from django.db import models

# Create your models here.

class topToolbar(models.Model):
    site_email = models.EmailField()
    site_address = models.TextField()
    site_contact = models.PositiveIntegerField()

    def __str__(self) -> str:
        return "Main Toolbar Content"