from rest_framework import serializers

class SchemaTenantDomainSerializer(serializers.Serializer):
    business_name = serializers.CharField( required =True)
    business_email = serializers.EmailField(required =True)
    domain_name = serializers.CharField( required =True)
    password = serializers.CharField(write_only = True, required =True)
    confirm_password = serializers.CharField(write_only = True, required = True)

    def validate_domain_name(self, value):
        if '-' in value or '_' in value:
            raise serializers.ValidationError('Domain name should not contain either - or _')
        return value
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError('password do not match')
        return super().validate(attrs)


