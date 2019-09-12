# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from uuid import uuid1
from rest_framework import serializers
from squan.api.models.customers import Customers
"""
Serializer fields handle convertion between primitive values and
internal datatypes. It also deals with validating input values,
as well as retrieving and setting the values from the parent object.
"""


# Customer serialization
class CustomerSerializer(serializers.Serializer):
    """
    Customer Serializer deals with all the fields related to the customer
    All the fields with auto_now are readOnly be default, in this serialization
    the field date is read only.
    """
    id = serializers.UUIDField(default=uuid1)
    firstname = serializers.CharField(read_only=False, required=True)
    surname = serializers.CharField(read_only=False, required=True)
    email = serializers.CharField(read_only=False, required=True)
    phone = serializers.IntegerField(read_only=False, required=True)
    dateAdded = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    def create(self, validated_data):
        """
        Data is getting serialized and validated before it saved in the database
        """
        return Customers.objects.create(**validated_data)