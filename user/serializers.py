from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class SigninSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'nickname']  
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user