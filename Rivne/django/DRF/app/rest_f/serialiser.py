from rest_framework import serializers
from .models import UserList, Address
from .validator import AddressValidator


class AddressListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['id', 'country', 'city', 'zip_code', 'street', 'house_num', 'apartaments']
        validators = [AddressValidator()]

    def create(self, validated_data):
        result = Address.objects.create(**validated_data)
        return result

    def update(self, instance, validated_data):
        instance.country = validated_data.get('country', instance)
        instance.city = validated_data.get('city', instance)
        instance.zip_code = validated_data.get('zip_code', instance)
        instance.street = validated_data.get('street', instance)
        instance.house_num = validated_data.get('house_num', instance)
        instance.apartaments = validated_data.get('apartaments', instance)
        instance.save()
        return instance


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserList
        fields = ['id', 'username', 'email', 'address']

