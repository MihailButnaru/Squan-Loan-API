# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from squan.api.models.customers import Customers
from squan.api.serializers.customer_serializer import CustomerSerializer

class CustomersList(APIView):
    """ Shows a list customers, allows to create a new customer """
    def get(self, request, format=None):
        """ Returns a list of customers """
        customers = Customers.objects.all()
        cus_serializer = CustomerSerializer(customers, many=True)
        return Response({'customers': cus_serializer.data})
