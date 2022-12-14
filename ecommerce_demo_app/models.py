from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField()
    image = models.ImageField(upload_to='product_picture')
