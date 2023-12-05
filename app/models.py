from django.db import models
import datetime 

# **CATEGORY** of foam shapes
class Shape(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='uploads/product/', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.name
    
# Customers
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

# Types of foam **PRODUCT** material
class Material(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    shapes = models.ManyToManyField(Shape)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
 
# Customer Orders
class Order(models.Model):
    material = models.ForeignKey(Material, default=1, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.material


