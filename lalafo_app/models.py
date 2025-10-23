
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    phone = PhoneNumberField()
    description = models.TextField()
    product_type = models.BooleanField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to='product_images')


    def __str__(self):
        return self.product_name