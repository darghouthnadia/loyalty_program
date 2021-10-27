from .models import DiscountCode, Brand, Follower
from rest_framework import serializers

class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class FollowerSerializer(serializers.ModelSerializer):
    discount_code = DiscountCodeSerializer(read_only=True, many=True)
    class Meta:
        model= Follower
        fields= ('id_user', 'discount_code',)