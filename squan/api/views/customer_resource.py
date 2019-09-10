# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from django.shortcuts import render
from rest_framework import generics

class CustomerView(generics.RetrieveUpdateDestroyAPIView):
    pass