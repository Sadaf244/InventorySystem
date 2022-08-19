from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=150,null=False, blank=False)
    product_price=models.FloatField(null=False, blank=False)
    product_description = models.CharField(max_length=150,null=False, blank=False)
    inventory_count=models.IntegerField(null=False, blank=False)
    
    
