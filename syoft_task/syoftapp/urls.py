from django.urls import path
from .views import *

urlpatterns = [
    path('ProductCreate/',ProductCreateView.as_view(), name='ProductCreateView'),#api for Creating the Product 
    #http://localhost:8000/product/ProductCreate/
    
    path('Product_List_Update/',Product_List_Update),#api for Product List and Update
    #http://localhost:8000/product/Product_List_Update/?product_id=1

    path('ProductDelete/<int:pk>',ProductDeleteView.as_view(), name='ProductDeleteView'), #api for Delete  The Product 
    #http://localhost:8000/product/ProductDelete/  
    
    
]
