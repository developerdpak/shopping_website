from django.contrib.auth.models import User
from django.db import models

# Create your models here.

STATE_CHOICES = (
    ('Andaman& Nicobar Islands', 'Andaman& Nicobar Islands'),
    ('Goa', 'Goa'),
    ('Karela', 'Karela'),
    ('Bihar', 'Bihar'),
    ('Chandigarh', 'Chandigarh'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('West Bengal', 'West Bengal'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Haryana', 'Haryana'),
    ('Punjab', 'Pujab'),
    ('Manipur', 'Manipur'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=264)
    locality = models.CharField(max_length=264)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TV', 'Television'),
    ('WM', 'WashingMachine'),
)


class Product(models.Model):
    title = models.CharField(max_length=264)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    brand = models.CharField(max_length=264)
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    product_image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return str(self.id)
