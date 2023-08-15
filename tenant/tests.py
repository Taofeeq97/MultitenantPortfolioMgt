# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from django.urls import reverse
# from .models import Tenant, Domain
# from client.models import BusinessAcount
# from .serializer import SchemaTenantDomainSerializer

# class CreateTenantAPIViewTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.url = reverse('create_tenant')

#     def test_create_valid_tenant(self):
#         payload = {
#             'business_name': 'TestBusiness',
#             'business_email': 'test@example.com',
#             'domain_name': 'test-domain',
#             'password': 'testpassword'
#         }

#         response = self.client.post(self.url, payload, format='json')

#         self.assertEqual(Tenant.objects.count(), 1)
#         self.assertEqual(BusinessAcount.objects.count(), 1)
#         self.assertEqual(Domain.objects.count(), 1)

#         tenant = Tenant.objects.get(schema_name='Test Business')
#         business_account = BusinessAcount.objects.get(email='test@example.com')
#         domain = Domain.objects.get(tenant=tenant, is_primary=True)

#         self.assertEqual(tenant.portfolio_name, 'TestBusiness')
#         self.assertEqual(business_account.business_name, 'Test Business')
#         self.assertEqual(business_account.username, 'test@example.com')
#         self.assertEqual(domain.domain, 'test-domain.web-production-a587.up.railway.app')

    # def test_create_invalid_tenant(self):
    #     payload = {
    #         # Missing required fields
    #         'business_email': 'test@example.com',
    #         'domain_name': 'test-domain',
    #         'password': 'testpassword'
    #     }

    #     response = self.client.post(self.url, payload, format='json')

    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertEqual(Tenant.objects.count(), 0)
    #     self.assertEqual(BusinessAccount.objects.count(), 0)
    #     self.assertEqual(Domain.objects.count(), 0)

    #     # Additional assertions to test the response data structure
    #     self.assertIn('status', response.data)
    #     self.assertIn('responseCode', response.data)
    #     self.assertEqual(response.data['responseCode'], status.HTTP_400_BAD_REQUEST)
    #     self.assertIn('message', response.data)
    #     self.assertIn('data', response.data)
    #     self.assertFalse(response.data['status'])

    # # Add more test cases as needed

