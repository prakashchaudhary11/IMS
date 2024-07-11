from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    username = models.CharField(max_length=300,default='username')


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class ProductType(models.Model):
    name = models.CharField(max_length=300)

class Department(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    type = models.ForeignKey(ProductType, on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    department = models.ManyToManyField(Department,null=True)

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    ceo = models.CharField(max_length=50)

class Purchase(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    supplier = models.ForeignKey(Supplier,on_delete=models.SET_NULL,null=True)

class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

class Sell(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)







