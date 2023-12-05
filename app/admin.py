from django.contrib import admin
from .models import Shape, Customer, Material, Order

# Register your models here.

admin.site.register(Shape)
admin.site.register(Customer)
admin.site.register(Material)
admin.site.register(Order)
