from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['Username','Email', 'Password']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, valdiated_data):
        user = User.objects.create_user(

            username = valdiated_data['username'],
            email = valdiated_data['email'],
            password = valdiated_data['password']
        
        ) 
        return user


class RecipesSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Recipe
        fields = '__all__'
        read_only_fields = ('id', 'user', 'Created_Date')