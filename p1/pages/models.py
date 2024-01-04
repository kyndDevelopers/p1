from django.db import models

# Create your models here.

class Newpage(models.Model):
    page_title = models.CharField(max_length=200)
    page_content = models.TextField()
    
    def __str__(self) -> str:
        return self.page_title
