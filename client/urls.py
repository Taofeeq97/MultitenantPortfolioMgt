from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('login/', views.ObtainTokenPairApiView.as_view(), name = 'token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create_client_portfolio/', views.CreateClientPortfolioAPIView.as_view(), name='create_client_portfolio'),
    path('client_list/', views.ClientPortfolioListAPIView.as_view(), name='client_list'),
    path('industry_list/', views.ClientIndustryListAPIView.as_view(), name='industry_list'),
]