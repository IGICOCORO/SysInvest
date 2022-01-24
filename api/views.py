from typing import List

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from .models import *

class TokenPairView(TokenObtainPairView):
	serializer_class = TokenPairSerializer

class ComptePrincipalViewset(viewsets.ModelViewSet):
	serializer_class = ComptePrincipalSerializer
	queryset = ComptePrincipal.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]


class ParcelleViewset(viewsets.ModelViewSet):
	serializer_class = ParcelleSerializer
	queryset = Parcelle.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class MotoViewset(viewsets.ModelViewSet):
	serializer_class = MotoSerializer
	queryset = Moto.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class CreditViewset(viewsets.ModelViewSet):
	serializer_class = CreditSerializer
	queryset = Credit.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class AutresInvestissementViewset(viewsets.ModelViewSet):
	serializer_class = AutresInvestissementSerializer
	queryset = AutresInvestissement.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]


class VehiculesLocalesViewset(viewsets.ModelViewSet):
	serializer_class = VehiculesLocalesSerializer
	queryset = VehiculesLocales.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class ImportesJaponToDarEsViewset(viewsets.ModelViewSet):
	serializer_class = ImportesJaponToDarEsSerializer
	queryset = ImportesJaponToDarEs.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class ImportesDarEsToBujaViewset(viewsets.ModelViewSet):
	serializer_class = ImportesDarEsToBujaSerializer
	queryset = ImportesDarEsToBuja.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
	