from rest_framework import serializers
from .models import ClientPortfolio, ClientIndustry, BusinessAcount
from rest_framework_simplejwt.tokens import RefreshToken

class ClienTIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientIndustry
        fields = '__all__'


class ClientPortfolioSerializer(serializers.ModelSerializer):
    client_industry = ClienTIndustrySerializer()  # Nested serializer for the dropdown

    class Meta:
        model = ClientPortfolio
        fields = ('client_first_name', 'client_last_name', 'client_email', 'client_industry', 'client_security_question', 'client_security_answer', 'total_investment')
        extra_kwargs = {
            'client_security_question': {'write_only': True},
            'client_security_answer': {'write_only': True}
        }

   
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def get_token(self, user):
        refresh = RefreshToken.for_user(user)
        token = str(refresh.access_token)
        return token

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = BusinessAcount.objects.filter(email=email).first()
        if not user or not user.check_password(password):
            raise serializers.ValidationError('Invalid login credentials or not a verified user')
        token = self.get_token(user)
        response = {
            'email': email,
            'first_name':user.first_name,
            # 'profile_picture': user.profile_picture.url,
            'last_name': user.last_name,
            'token': token,
        }
        return response
        
