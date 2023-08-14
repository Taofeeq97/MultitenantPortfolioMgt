from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .models import ClientPortfolio, ClientIndustry
from .serializers import ClientPortfolioSerializer, LoginSerializer, ClienTIndustrySerializer
from collections import defaultdict
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

# # Create your views here.
class ObtainTokenPairApiView(TokenObtainPairView):
    """
    An endpoint to obtain Access token

    """
    serializer_class = LoginSerializer



class CreateClientPortfolioAPIView(generics.CreateAPIView):
    queryset = ClientPortfolio.objects.all()
    serializer_class = ClientPortfolioSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': True,
                'responseCode':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'Client portfolio created successfully'
            }
            return Response(response_data) 
        else:
            response_data = {
                'status':False,
                'responseCode':status.HTTP_400_BAD_REQUEST,
                'errors':serializer.errors,
                'message': 'error occured while creating client portfolio'
            }
            return Response(response_data)
            

class ClientPortfolioListAPIView(generics.ListAPIView):
    queryset = ClientPortfolio.objects.all()
    serializer_class = ClientPortfolioSerializer
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        industry_stats = defaultdict(lambda: {'count': 0, 'total_investment': 0})

        for instance in serializer.data:
            industry_name = instance['client_industry']['industry_name']
            investment = instance['total_investment']

            industry_stats[industry_name]['count'] += 1
            industry_stats[industry_name]['total_investment'] += investment

        response_data = {
            'status': True,
            'responseCode': status.HTTP_200_OK,
            'data': serializer.data,
            'industry_stats': dict(industry_stats),  
            'message': 'Client portfolio retrieved successfully'
        }
        return Response(response_data)
        

class ClientIndustryListAPIView(generics.ListAPIView):
    serializer_class = ClienTIndustrySerializer
    queryset = ClientIndustry.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        response_data = {
            'status': True,
            'responseCode': status.HTTP_200_OK,
            'data': serializer.data, 
            'message': 'Client industries retrieved successfully'
        }
        return Response(response_data)


class CreateClientIndustryAPIView(generics.CreateAPIView):
    queryset = ClientIndustry.objects.all()
    serializer_class = ClienTIndustrySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': True,
                'responseCode':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'Client industry created successfully'
            }
            return Response(response_data) 
        else:
            response_data = {
                'status':False,
                'responseCode':status.HTTP_400_BAD_REQUEST,
                'errors':serializer.errors,
                'message': 'error occured while creating client industry'
            }
            return Response(response_data)
    
