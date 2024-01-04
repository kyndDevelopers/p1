from django.db import models

# Create your models here.

class Newarticle(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_content = models.TextField()
    is_popular = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.blog_title
    

class Categories(models.Model):
    category_name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.category_name


class Tags(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tag_name