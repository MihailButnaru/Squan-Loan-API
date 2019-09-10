# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from uuid import uuid1
from django.conf import settings
from django.db import models
"""
Customer model view
"""

class Customers(models.Model):
    client_id = models.UUIDField(
            primary_key=True, 
            default=uuid1, 
            editable=False, 
            verbose_name=('clientId'))
    firstname = models.TextField(
            max_length=20, 
            null=False, 
            blank=False)
    surname = models.TextField(
            max_length=20, 
            null=False, 
            blank=False)
    email = models.TextField(
            max_length=20, 
            null=False, 
            blank=False)
    phone = models.IntegerField(
            null=False, 
            blank=False)
    date = models.DateTimeField(
            auto_now_add=True,
            verbose_name=('created')
    )

    class Meta:
        db_table = 'customers'