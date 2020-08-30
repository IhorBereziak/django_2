from rest_framework import serializers

from .models import OfficeModel, CityModel

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CityModel
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficeModel
        fields = '__all__'