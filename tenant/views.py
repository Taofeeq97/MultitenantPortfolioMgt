from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import SchemaTenantDomainSerializer
from .models import Tenant, Domain
from client.models import BusinessAcount
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class CreateTenantAPIView(APIView):

    serializer = SchemaTenantDomainSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer(data = request.data)
        if serializer.is_valid():
            business_name = serializer.validated_data.get('business_name')
            business_email = serializer.validated_data.get('business_email')
            domain_name = serializer.validated_data.get('domain_name')
            password = serializer.validated_data.get('password')

            tenant = Tenant(schema_name=business_name,
                            portfolio_name=business_name,
                            )

            business_account = BusinessAcount.objects.create(
                business_name = business_name,
                email = business_email,
                username = business_email,
            )

            tenant.business_owner = business_account
            tenant.save()

            business_account.set_password(password)
            domain = Domain()
            domain.domain = domain_name+'.web-production-a587.up.railway.app'
            domain.tenant = tenant
            domain.is_primary = True
            domain.save()

            response_data = {
                'status': True,
                'responseCode':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'Organization structure retrieved successfully'
            }
            return Response(response_data)
        
        else:
            response_data = {
                'status': True,
                'responseCode':status.HTTP_400_BAD_REQUEST,
                'data':serializer.errors,
                'message':'error occured while creating tenant'
            }
            return Response(response_data)
        




