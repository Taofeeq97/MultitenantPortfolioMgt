from django.db import models
from django.contrib.auth.models import User
from django_tenants.models import DomainMixin, TenantMixin
from client.models import BusinessAcount


class Tenant(TenantMixin):
    business_owner = models.ForeignKey(BusinessAcount, on_delete=models.CASCADE, null=True)
    portfolio_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False, blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    # default true, schema will be automatically created and
    # synced when it is saved
    auto_create_schema = True

    # """
    # USE THIS WITH CAUTION!
    # Set this flag to true on a parent class if you want the schema to be
    # automatically deleted if the tenant row gets deleted.
    # """
    # auto_drop_schema = True


    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.portfolio_name}"


class Domain(DomainMixin):
    pass