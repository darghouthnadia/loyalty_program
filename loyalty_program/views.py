from rest_framework.response import Response
from .serializers import BrandSerializer, DiscountCodeSerializer, FollowerSerializer
from rest_framework import serializers, viewsets, status
from rest_framework import authentication
from .models import DiscountCode, Brand, Follower
import string    
import random
from django.http import HttpResponse

class  ListDiscountCode(viewsets.ViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = []

    def generate(self, request):
        id_brand = request.data.get('id_brand')
        number_of_dicount_codes = int(request.data.get('number_of_dicount_codes'))
        # add validation for brand here
        if(number_of_dicount_codes <= 0): 
            return HttpResponse(status=403)
        self.createXdiscountCodes(number_of_dicount_codes, id_brand)
        # Publish to rabbit MQ here for brand/store and search service that new codes are available 
        return HttpResponse(status=200)

    def list(self, request):
        dicount_codes = DiscountCode.objects.all()
        serializer= DiscountCodeSerializer(dicount_codes, many=True)
        return Response(serializer.data)

    def createXdiscountCodes(self, x, id_brand):
        for iteration in range(0, x):
            # made a decision here that all codes are just 4 digits, this is not how it should be in real life
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            if(DiscountCode.objects.filter(brand=id_brand, value=code).exists()):
                return self.createXdiscountCodes(x, id_brand)
            else:
                discountCode = {"value": code, "brand": id_brand}
                serializer = DiscountCodeSerializer(data=discountCode)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                x = x -iteration
        return  HttpResponse(status=201)


class  BrandView(viewsets.ViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = []

    def create(self, request):
        serializer = BrandSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def list(self, request):
        brands = Brand.objects.all()
        serializer= BrandSerializer(brands, many=True)
        return Response(serializer.data)

class  FollowerView(viewsets.ViewSet):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = []

        
    def list(self, request):
        followers = Follower.objects.all()
        serializer= FollowerSerializer(followers)
        return Response(serializer.data)
    
    def retreive(self, request):
        id_user = request.data.get('user') 
        brand = request.data.get('brand')
        code = request.data.get('code')
        discount_code = DiscountCode.objects.get(value=code, brand=brand)
        Follower.objects.create(id_user=id_user, discount_code=discount_code)
        # Add here call to rabbitMQ to publish event that a user reclaimed a discount code and thus becoming a fellower
        serializer = DiscountCodeSerializer(discount_code)
        return Response(serializer.data)
    