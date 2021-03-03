from .models import *
from rest_framework import serializers




class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model =Blogpost
        fields ='__all__'