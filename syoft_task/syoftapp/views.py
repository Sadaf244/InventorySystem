from .serializers import *
from rest_framework import generics, status
from rest_framework.decorators import api_view
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status,permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from UserAccount.permissions import *


class ProductCreateView(generics.CreateAPIView): #to create Product
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated&IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@api_view(['GET', 'DELETE','PUT'])
def Product_List_Update(request):
    user=request.user
    if user.role=='Admin' or user.role=='Manager':
        try:
            product = Product.objects.all() #get all product details
            if not product:
                return Response({'message': 'The product list is empty'}, status=status.HTTP_404_NOT_FOUND) 
            product_id= request.GET.get('product_id', None)  #get ID from parameter of url if specified
            if product_id is not None:
                product = product.filter(id=product_id)  #get that specific product  from ID
            if not product:
                return Response({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        except Product.DoesNotExist: 
            return Response({'message': 'The product model does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    # retrieve specific data or all
        if request.method == 'GET': 
            product_serializer = ProductSerializer(product, many=True)
            return Response(product_serializer.data)
    # delete specific data or all
        elif request.method == 'DELETE':
            product.delete() 
            return Response({'message': 'Product record was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'PUT':
            product = product.filter(id=product_id).first() #get first entry of product with that id
            serializer=ProductSerializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    else:
        return Response({'message': 'You have no permission !'},status=status.HTTP_400_BAD_REQUEST) 

 
class ProductDeleteView(generics.DestroyAPIView): #to Delete Product
    authentication_classes=[JWTAuthentication]
    permission_classes=[permissions.IsAuthenticated&IsAdminUser]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
