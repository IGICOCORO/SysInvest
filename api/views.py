from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.db import transaction

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

	def create(self,request):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = request.data
		comptes = ComptePrincipal.objects.all()
		if comptes:
			compte:ComptePrincipal = comptes.first()
			compte.montant += int(data["montant"])
			compte.save()
			serializer = ComptePrincipalSerializer(compte, many=False)
		else:
			serializer.save()
		return Response(serializer.data,201)


class ParcelleViewset(viewsets.ModelViewSet):
	serializer_class = ParcelleSerializer
	queryset = Parcelle.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@transaction.atomic
	def create(self, request, *args, **kwargs): 
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = request.data
		compte:ComptePrincipal = ComptePrincipal.objects.first()
		compte.solde -= int(data['prix_achat_par_are'])
		compte.solde -= int(data['autres_depenses'])
		compte.save()
		serializer.save()
		return Response(serializer.data,201)

class MotoViewset(viewsets.ModelViewSet):
	serializer_class = MotoSerializer
	queryset = Moto.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@transaction.atomic
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = request.data
		compte:ComptePrincipal = ComptePrincipal.objects.first()
		compte.solde -= int(data["prix_achat_unitaire"])
		compte.solde -= int(data['autres_depenses'])
		compte.save()
		serializer.save()
		return Response(serializer.data,201)


class CreditViewset(viewsets.ModelViewSet):
	serializer_class = CreditSerializer
	queryset = Credit.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@transaction.atomic
	def create(self, request, *args, **kwargs): 
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = request.data
		compte:ComptePrincipal = ComptePrincipal.objects.first()
		compte.solde -= int(data['montant'])
		compte.save()
		serializer.save()
		return Response(serializer.data,201)

class AutresInvestissementViewset(viewsets.ModelViewSet):
	serializer_class = AutresInvestissementSerializer
	queryset = AutresInvestissement.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

	@transaction.atomic
	def create(self, request, *args, **kwargs): 
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = request.data
		compte:ComptePrincipal = ComptePrincipal.objects.first()
		compte.solde -= int(data['montant_investi'])
		compte.save()
		serializer.save()
		return Response(serializer.data,201)


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

class IncomeViewset(viewsets.ModelViewSet):
	serializer_class = IncomeSerializer
	queryset = Income.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class OutcomeViewset(viewsets.ModelViewSet):
	serializer_class = OutcomeSerializer
	queryset = Outcome.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]
	
class PretViewset(viewsets.ModelViewSet):
	serializer_class = PretSerializer
	queryset = Pret.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]

class EmpruntViewset(viewsets.ModelViewSet):
	serializer_class = EmpruntSerializer
	queryset = Emprunt.objects.all()
	authentication_classes = [JWTAuthentication, SessionAuthentication]
	permission_classes = [IsAuthenticated]			