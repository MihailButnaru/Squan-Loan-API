# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from django.db import models

class Loans(models.Model):
    """ Loan model """
    id = models.UUIDField(primary_key=True, editable=False)
    client_id = models.UUIDField(null=False)
    amount = models.IntegerField(null=False)
    term = models.IntegerField(null=False)
    rate = models.FloatField(null=False)
    date = models.DateTimeField(auto_now_add=True, verbose_name=('created'))

    class Meta:
        verbose_name = 'loan'
        verbose_name_plural = 'loans'
        db_table = 'loans'