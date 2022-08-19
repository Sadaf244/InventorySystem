from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_price','product_description','inventory_count']
admin.site.register(Product,ProductAdmin)
