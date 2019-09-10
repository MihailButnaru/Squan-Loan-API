# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from uuid import uuid1
from django.conf import settings
from django.db import models

class Customers(models.Model):
    """ Customer model """
    firstname = models.TextField(max_length=20, null=False)
    surname = models.TextField(max_length=20, null=False)
    email = models.TextField(max_length=20, null=False)
    phone = models.IntegerField()
    dateAdded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.surname)

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        db_table = 'customers'