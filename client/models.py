from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from base.manager import UserManager, OrganizationManager
# Create your models here.

class BusinessAcount(AbstractUser, PermissionsMixin):
    business_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, verbose_name='Email Address')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        indexes = [ models.Index(fields=['email'])]
       
    def __str__(self):
        return self.email
    

class ClientIndustry(models.Model):
    industry_name = models.CharField(max_length=100)
    industry_description = models.TextField()

    def __str__(self):
        return self.industry_name
    
    
class ClientPortfolio(models.Model):
    client_first_name = models.CharField(max_length=100)
    client_last_name = models.CharField(max_length=100)
    client_gender = models.CharField(max_length=10, blank=True, null=True)
    client_industry = models.ForeignKey(ClientIndustry, on_delete=models.CASCADE)
    client_profile_picture = models.ImageField(upload_to='media')
    client_email = models.EmailField(unique=True, verbose_name='Email Address')
    client_security_question = models.CharField(max_length=100)
    client_security_answer = models.CharField(max_length=100)
    total_investment = models.IntegerField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)

       
    def __str__(self):
        return self.client_email


class Organization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class OrganizationalUnit(models.Model):
    name = models.CharField(max_length=50)
    parent_unit = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = OrganizationManager()

    def __str__(self):
        return self.name

