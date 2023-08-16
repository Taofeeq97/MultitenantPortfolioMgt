from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


    
    
class OrganizationManager(models.Manager):
   
   def get_active_organizations(self):
      return self.filter(is_approved=True)
   
   def get_latest_created(self):
      return self.order_by('-created_at')
   
   


class DeletedManager(models.Manager):
 def get_queryset(self):
    return super(DeletedManager, self).get_queryset().filter(is_deleted=True)