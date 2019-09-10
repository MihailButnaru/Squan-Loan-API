# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from rest_framework import serializers
from squan.api.models.customers import Customers
"""
Serializer fields handle convertion between primitive values and
internal datatypes. It also deals with validating input values,
as well as retrieving and setting the values from the parent object.
"""


# Customer serialization
class CustomerSerializer(serializers.ModelSerializer):
    """
    Customer Serializer deals with all the fields related to the customer
    All the fields with auto_now are readOnly be default, in this serialization
    the field date is read only.
    """
    class Meta:
        model = Customers
        fields = ('pk', 'firstname', 'surname', 'email', 'phone', 'dateAdded')
        depth = 0

