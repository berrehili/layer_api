from rest_framework import serializers
from layer_api.models import UserInfos
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('lastname','birthday','email','password','phone')

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')

# class InfosSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInfos
#         fields = ('firstname','lastname','birthday','email','phone_number')