__author__ = 'dimitris'
from rest_framework import serializers
from models import Product,ProductImage

class PicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image','main']