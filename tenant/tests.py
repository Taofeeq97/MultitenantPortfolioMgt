from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Tenant, BusinessAccount, Domain
from .serializer import SchemaTenantDomainSerializer

class CreateTenantAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = ''

    def test_create_tenant(self):
        payload = {
            'business_name': 'Test Business',
            'business_email': 'test@example.com',
            'domain_name': 'test-domain',
            'password': 'testpassword'
        }
        
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        tenant = Tenant.objects.get(schema_name='Test Business')
        business_account = BusinessAccount.objects.get(email='test@example.com')
        domain = Domain.objects.get(tenant=tenant, is_primary=True)

        self.assertEqual(tenant.portfolio_name, 'Test Business')
        self.assertEqual(business_account.business_name, 'Test Business')
        self.assertEqual(business_account.username, 'test@example.com')
        self.assertTrue(business_account.check_password('testpassword'))
        self.assertEqual(domain.domain, 'test-domain.web-production-a587.up.railway.app')

    def test_create_tenant_invalid_data(self):
        payload = {
            # Missing required fields
            'business_email': 'test@example.com',
            'domain_name': 'test-domain',
            'password': 'testpassword'
        }
        
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        # Additional assertions to test the response data structure
        self.assertIn('status', response.data)
        self.assertIn('responseCode', response.data)
        self.assertEqual('responseCode', 400)
        self.assertIn('message', response.data)
        self.assertIn('data', response.data)
        self.assertFalse(response.data['status'])

    # Add more test cases as needed
