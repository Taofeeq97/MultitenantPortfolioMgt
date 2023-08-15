from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import ClientPortfolio, Organization
from .serializers import ClientPortfolioSerializer

class CreateOrganizationAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create_organization')

    def test_create_valid_organization(self):
        payload = {
            'name': 'AFEX',
        }
        response = self.client.post(self.url, payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Organization.objects.count(), 1)


        
# class CreateClientPortfolioAPIViewTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.url = reverse('create_client_portfolio')

#     def test_create_valid_client_portfolio(self):
#         payload = {
#             'client_first_name': 'John',
#             'client_last_name': 'Doe',
#             'client_gender': 'Male',
#             'client_industry': 1,  # Replace with a valid industry ID
#             'client_email': 'john@example.com',
#             'client_security_question': 'Question',
#             'client_security_answer': 'Answer',
#             'total_investment': 5000,
#             'status': True
#         }

#         response = self.client.post(self.url, payload, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(ClientPortfolio.objects.count(), 1)

#     def test_create_invalid_client_portfolio(self):
#         payload = {
#             # Missing required fields
#             'client_last_name': 'Doe',
#             'client_gender': 'Male',
#             'client_email': 'john@example.com',
#             'client_security_question': 'Question',
#             'client_security_answer': 'Answer',
#             'total_investment': 5000,
#             'status': True
#         }

#         response = self.client.post(self.url, payload, format='json')

#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(ClientPortfolio.objects.count(), 0)

#         # Additional assertions to test the response data structure
#         self.assertIn('status', response.data)
#         self.assertIn('responseCode', response.data)
#         self.assertEqual(response.data['responseCode'], status.HTTP_400_BAD_REQUEST)
#         self.assertIn('message', response.data)
#         self.assertIn('errors', response.data)
#         self.assertFalse(response.data['status'])

#     # Add more test cases as needed
