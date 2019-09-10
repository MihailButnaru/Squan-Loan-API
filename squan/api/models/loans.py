# Copyright | 2019 | All rights reserved
# MIHAIL BUTNARU
from django.db import models
"""
Loan model view
"""

class Loans(models.Model):
    client_id = models.UUIDField(primary_key=True, editable=False)
    amount = models.IntegerField(null=False)
    term = models.IntegerField(null=False)
    rate = models.FloatField(null=False)
    date = models.DateTimeField(auto_now_add=True, verbose_name=('created'))

    class Meta:
        db_table = 'loans'