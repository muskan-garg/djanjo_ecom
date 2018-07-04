from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categories(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Categories)
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,null='True')
    pic=models.FileField(upload_to='pic',null='True')
    description=models.TextField(blank='True')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.name
class Info(models.Model):
    user = models.OneToOneField(User)
    pic= models.FileField(upload_to='pic',null=True)
class Cart(models.Model):
    product=models.ForeignKey(Product)
    quantity=models.IntegerField()
    total_price=models.FloatField()
    def __str__(self):
        return self.product.name
class Profile(models.Model):
    country_choices = (
    ('IN','India'),
    ('US','United States'),
    ('CH','China'),
    ('UK','United Kingdom'),
    )
    fname=models.CharField(max_length=30,null='True')
    lname=models.CharField(max_length=30,null='True')
    cname=models.CharField(max_length=30,null='True')
    email=models.EmailField(max_length=30,null='True')
    country=models.CharField(max_length=2,choices=country_choices,null=True)
    address=models.CharField(max_length=30,null='True')
    town=models.CharField(max_length=30,null='True')
    zip_code=models.IntegerField(null='True')
    ph_number=models.IntegerField(null='True')
    comment=models.TextField(max_length=30,null='True')
    def __str__(self):
        return self.fname
