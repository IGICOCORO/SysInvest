from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ComptePrincipal)
class ComptePrincipal(admin.ModelAdmin):
	list_display = "solde",
	search_fields = "id",
@admin.register(Parcelle)
class Parcelle(admin.ModelAdmin):
	list_display = "nombres_ares","prix_achat_par_are","date_achat","autres_depenses","lieu","date_vente_previ","prix_vente_previ"
	search_fields = "nombres_ares","prix_achat_par_are","lieu",

@admin.register(Moto)
class Moto(admin.ModelAdmin):
	list_display = "quantite","prix_achat_unitaire","date_achat","date_vente_previ","prix_vente_unitaire_previ"
	search_fields = "quantite","date_vente_previ",
@admin.register(Credit)
class Credit(admin.ModelAdmin):
	list_display = "nom_demandeur","montant","interet_total","date_debut_credit","nombre_jours_total","delais_recuperation"
	search_fields = "delais_recuperation","nom_demandeur",

@admin.register(AutresInvestissement)
class AutresInvestissement(admin.ModelAdmin):
	list_display = "nom_investissement","montant_investi","date_investissement","benefice","date_fin_investissement"
	search_fields = "nom_investissement",


@admin.register(VehiculesLocales)
class VehiculesLocales(admin.ModelAdmin):
	list_display = "modele","plaque","prix_achat","date_achat","autres_depenses","details","date_vente_previ","prix_vente_previ"
	search_fields = "plaque","modele",


@admin.register(ImportesJaponToDarEs)
class ImportesJaponToDarEs(admin.ModelAdmin):
	list_display = "modele","numero_chasis","prix_achat_et_transport","taux_echange","date_achat","date_arrivee"
	search_fields = "numero_chasis","modele",

@admin.register(ImportesDarEsToBuja)
class ImportesDarEsToBuja(admin.ModelAdmin):
	list_display = "Dédouanement","transport","taux","autre_dépenses","details","date","prix_vente_previ"
	search_fields = "Dédouanement","transport",

@admin.register(Income)
class Income(admin.ModelAdmin):
	list_display = "source","montant","partenaire","date"
	search_fields = "source","partenaire",


@admin.register(Outcome)
class Outcome(admin.ModelAdmin):
	list_display = "raison","montant","partenaire","date"
	search_fields = "raison","montant","partenaire"

@admin.register(Dette)
class Dette(admin.ModelAdmin):
	list_display = "nom","montant","date"
	search_fields = "nom","montant",