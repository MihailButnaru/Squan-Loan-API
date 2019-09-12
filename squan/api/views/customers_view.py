# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
import json
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from squan.api.models.customers import Customers
from squan.api.serializers.customer_serializer import CustomerSerializer

from rest_framework import generics, mixins


class CustomersList(APIView):
    """ Shows a list customers, allows to create a new customer """
    def get(self, request, format=None):
        """ Returns a list of customers """
        customers = Customers.objects.all()
        cus_serializer = CustomerSerializer(customers, many=True)
        return Response({'customers': cus_serializer.data})

    @swagger_auto_schema(responses={201: CustomerSerializer(),
                                    400: 'Invalid Data'})
    def post(self, request, *args, **kwargs):
        """ Create a customer """
        print(request.data)
        cus_serializer = CustomerSerializer(data=request.data)
        if cus_serializer.is_valid():
            cus_serializer.save()
            return Response({'customer': cus_serializer.data})
        return Response({'error' : cus_serializer.errors})


class CustomerDetail(APIView):
    """ Retrieve, update or delete a customer """

    def customer_helper(self, id):
        """ Returns the customer based on the id 
                Args:
                    id (int) : unique identifier
        """
        try:
            return Customers.objects.get(pk=id)
        except Exception:
            raise Http404

    def get(self, request, id, format=None):
        """ Returns the customer based on the id
                Args:
                    id (int) : unique identifier
        """
        serializer = CustomerSerializer(self.customer_helper(id))
        return Response({'customer': serializer.data})

    def delete(self, request, id, format=None):
        """ Delete a customer based on the id
                Args:
                    id (int) : unique identifier
        """
        customer = self.customer_helper(id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id, format=None):
        """ Edit a customer based on the id
                Args:
                    id (int) : unique identifier
        """
        customer = self.customer_helper(id)
        customer_serializer = CustomerSerializer(customer, data=request.data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return Response(customer_serializer.data)
        return Response()

    