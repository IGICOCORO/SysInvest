from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import *

class ComptePrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComptePrincipal
        fields = '__all__'

class ParcelleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parcelle
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = '__all__'

class CreditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credit
        fields = '__all__'

class AutresInvestissementSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutresInvestissement
        fields = '__all__'

class VehiculesLocalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculesLocales
        fields = '__all__'

class ImportesJaponToDarEsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportesJaponToDarEs
        fields = '__all__'

class ImportesDarEsToBujaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportesDarEsToBuja
        fields = '__all__'

    
class TokenPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenPairSerializer, self).validate(attrs)
        data['id'] = self.user.id
        data['first_name'] = self.user.first_name
        data['last_name'] = self.user.last_name

        return data
