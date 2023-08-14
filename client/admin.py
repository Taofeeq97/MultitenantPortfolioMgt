from django.contrib import admin
from .models import BusinessAcount, ClientPortfolio, ClientIndustry, Organization, OrganizationalUnit
# Register your models here.

admin.site.register(BusinessAcount)
admin.site.register(ClientPortfolio)
admin.site.register(ClientIndustry)
admin.site.register(Organization)
admin.site.register(OrganizationalUnit)