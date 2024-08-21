from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField('User phone number', max_length=60)


class Category(models.Model):

    name = models.CharField('Category name', max_length=60)

    def __str__(self):
        return self.name
    
class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat_prod')
    name = models.CharField('Product name', max_length=30)
    price = models.PositiveIntegerField('Product price')
    image = models.ImageField('Product image', upload_to='images')

    def __str__(self):
        return self.name