from django.db import models

# Create your models here.

# Choix des  Investissement
INVESTISSEMent_CHOICES = (
	("Parcelle","Parcelle"),
	("Transfert","Transfert"),
	("Véhicules","Véhicules"),
	("Motos","Motos"),
	("Credit","Credit"),
	("Autres investissments ","Autres investissments "),
	)

class ComptePrincipal(models.Model):
	id 	   = models.SmallAutoField()
	montant = models.PositiveBigIntegerField(default=0)

	def __str__(self):
		return f" Votre Capitale est {self.montant} "

class Parcelle(models.Model):
	id = models.SmallAutoField()
	nombres_ares = models.FloatField(default=0.0)
	prix_achat_par_are = models.PositiveBigIntegerField(default=0)
	date_achat = models.DateTimeField(auto_now_add=True)
	autres_depenses = models.PositiveBigIntegerField(default=0)
	lieu = models.CharField(max_length=60)
	details = models.TextField(max_length=70)
	date_vente_previ = models.DateField()
	prix_vente_previ = models.PositiveBigIntegerField(default=0)

	def__str__(self):
	   return f"{self.nombres_ares} acheté {self.prix_achat_par_are}Fbu et vendu {self.prix_vente_previ}"

class Motos(models.Model):
	id = models.SmallAutoField()
	quantite = models.PositiveIntegerField(default=0)
	prix_achat_unitaire = models.PositiveBigIntegerField(default=0)
	date_achat = models.DateTimeField(auto_now_add=True)
	autres_depenses = models.PositiveIntegerField(default=0)
	details = models.TextField(max_length=70)
	date_vente_previ = models.DateField()
	prix_vente_unitaire_previ = models.PositiveBigIntegerField(default=0)

	def__str__(self):
		return f"{self.quantite} acheté {self.prix_achat_unitaire} vendu { self.prix_vente_unitaire_previ}"

class Credit(models.Model):
	id = models.SmallAutoField()
	nom_demandeur = models.CharField(max_length=30)
	montant = models.PositiveBigIntegerField(default=0)
	interet_total = models.PositiveIntegerField(default=0)
	date_debut_credit = models.DateTimeField(auto_now_add=True)
	nombre_jours_total = models.CharField(max_length=30)
	delais_recuperation = models.DateField()
	details = models.TextField()
	def __str__(self):
		return f"{self.nom_demandeur} a {self.montant} remboursable dans { self.nombre_jours_total}"

class AutresInvestissement(models.Model):
	id = models.SmallAutoField()
	type_investissement = models.CharField(max_length=30)
	montant_investi = models.PositiveBigIntegerField()
	date_investissement = models.DateTimeField(auto_now_add=True)
	benefice = models.PositiveBigIntegerField(default=0)
	date_fin_investissement = models.DateField()


	def __str__(self):
		return f"{self.montant_investi} investi au {self.type_investissement} jusqu'au {self.date_fin_investissement}"

class VehiculesLocales(models.Model):
	id = models.SmallAutoField()
	modele = models.CharField(max_length=30)
	plaque = models.CharField(max_length=30)
	prix_achat = models.PositiveBigIntegerField(default=0)
	date_achat = models.DateTimeField(auto_now_add=True)
	autres_depenses = models.PositiveIntegerField(default=0)
	details = models.TextField()
	date_vente_previ = models.DateField()
	prix_vente_previ = models.PositiveBigIntegerField(default=0)

	def __str__(self):
		return f"{self.modele} { self.plaque} acheté {self.prix_achat} sera vendu { self.prix_vente_previ} au {self.date_vente_previ}"


class ImportesJaponToDarEs(models.Model):
	id = models.SmallAutoField()
	modele = models.CharField(max_length=30)
	numero_chasis = models.CharField(max_length=70)
	prix_achat_et_transport = models.PositiveBigIntegerField(default=0)
	taux_echange = models.PositiveIntegerField(default=0)
	date_achat = models.DateTimeField(auto_now_add=True)
	date_arrivee = models.DateField()

	def __str__(self):
		return f"{self.modele} achete le {self.date_achat} arrivera le {self.date_arrivee}"

class ImportesDarEsToBuja(models.Model):
	id = models.SmallAutoField()
	Dédouanement  = models.PositiveBigIntegerField(default=0)
	transport = models.PositiveBigIntegerField(default=0)
	taux= models.PositiveIntegerField(default=0)
	autre_dépenses= models.PositiveIntegerField(default=0)
	details = models.TextField()
	taux = models.DateTimeField(auto_now_add=True)
	prix_vente_previ= models.PositiveBigIntegerField(default=0)

	def __str__(self):
		return f"{self.Dédouanement} {self.taux} {self.taux} {self.prix_vente_previ}"