from rest_framework import viewsets, status
from rest_framework.response import Response

from products.producer import publish

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self, request): # /api/products
        products = Product.objects.all()
        print("PRODUCTS::::      ", products)
        serializer = ProductSerializer(products, many=True)
        print("PRODUCTS::::      ", serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request): # /api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(serializer.data['name'])
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None): # /api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
