from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20,verbose_name="name",unique=True)
    price=models.PositiveIntegerField(verbose_name="price")
    image=models.ImageField()

    def __str__(self):
        return self.name


