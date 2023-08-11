from django.contrib import admin
from .models import BusinessAcount, ClientPortfolio, ClientIndustry
# Register your models here.

admin.site.register(BusinessAcount)
admin.site.register(ClientPortfolio)
admin.site.register(ClientIndustry)