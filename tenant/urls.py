from django.urls import path
from . import views

urlpatterns = [
    path('create_business/', views.CreateTenantAPIView.as_view(), name='create_tenant')
]