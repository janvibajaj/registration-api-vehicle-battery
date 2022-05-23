from rest_framework import serializers
from .models import RegistrationList

class RegistrationListSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=70)
    number = serializers.IntegerField()
    email = serializers.EmailField(max_length=100)
    address = serializers.CharField(style={'base_template': 'textarea.html'})
    number_plate = serializers.CharField(max_length=20)
    type_of_vehicle = serializers.CharField(max_length=50)
    date = serializers.DateField()
    
    def create(self,validated_data):
        return RegistrationList.objects.create(**validated_data)
        
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.number = validated_data.get('number',instance.number)
        instance.email = validated_data.get('email',instance.email)
        instance.address = validated_data('address',instance.address)
        instance.number_plate = validated_data('number_plate',instance.number_plate)
        instance.type_of_vehicle = validated_data('type_of_vehicle', instance.type_of_vehicle)
        instance.date = validated_data('date',instance.date)
        instance.save()
        return instance