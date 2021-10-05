from base.serializers import ProductSerializer
from base.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response


from rest_framework import status

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products,many = True)
    return Response(serializers.data) 


@api_view(['GET'])
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    serializers = ProductSerializer(product,many=False)
    return Response(serializers.data)
