from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from base.manager import UserManager


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
    client_industry = models.ForeignKey(ClientIndustry, on_delete=models.CASCADE)
    client_profile_picture = models.ImageField(upload_to='media')
    client_email = models.EmailField(unique=True, verbose_name='Email Address')
    client_security_question = models.CharField(max_length=100)
    client_security_answer = models.CharField(max_length=100)
    total_investment = models.IntegerField()
       
    def __str__(self):
        return self.client_email
    