from django.contrib import admin

# Models
from squan.api.models.customers import Customers
from squan.api.models.loans import Loans

# Register your models here.
admin.site.register(Customers)
admin.site.register(Loans)