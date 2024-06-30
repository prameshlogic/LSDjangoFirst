from rest_framework import serializers
from .models import userModel

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = userModel
        fields = '__all__'
