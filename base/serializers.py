from rest_framework import serializers
from .models import *

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class RideModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideModel
        fields = '__all__'

