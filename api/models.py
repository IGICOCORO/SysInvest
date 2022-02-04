from django.db import models


# Choix des  Investissement
INVESTISSEMENT_CHOICES = (
	("Parcelle","Parcelle"),
	("Transfert","Transfert"),
	("Véhicules","Véhicules"),
	("Motos","Motos"),
	("Credit","Credit"),
	("Autres investissments ","Autres investissments "),
	)

class ComptePrincipal(models.Model):
	id 	 = models.AutoField(primary_key=True)
	montant = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f" Votre Capitale est {self.montant} "

class Parcelle(models.Model):
	id = models.AutoField(primary_key=True)
	nombres_ares = models.FloatField(default=0.0)
	prix_achat_par_are = models.PositiveBigIntegerField(default=0)
	date_achat = models.DateTimeField(auto_now_add=True)
	autres_depenses = models.PositiveBigIntegerField(default=0)
	lieu = models.CharField(max_length=60)
	details = models.TextField(max_length=70)
	date_vente_previ = models.DateField()
	prix_vente_previ = models.PositiveBigIntegerField(default=0)

	def __str__(self):
		return f"{self.nombres_ares} acheté {self.prix_achat_par_are}Fbu et vendu {self.prix_vente_previ}"

class Moto(models.Model):
	id = models.AutoField(primary_key=True)
	quantite = models.PositiveIntegerField(default=0)
	prix_achat_unitaire = models.PositiveBigIntegerField(default=0)
	date_achat = models.DateField(auto_now_add=True)
	autres_depenses = models.PositiveIntegerField(default=0)
	details = models.TextField(max_length=70)
	date_vente_previ = models.DateField()
	prix_vente_unitaire_previ = models.PositiveBigIntegerField(default=0)

	def __str__(self):
		return f"{self.quantite} acheté {self.prix_achat_unitaire} vendu { self.prix_vente_unitaire_previ}"

class Credit(models.Model):
	id = models.AutoField(primary_key=True)
	nom_demandeur = models.CharField(max_length=30)
	montant = models.PositiveBigIntegerField(default=0)
	interet_total = models.PositiveIntegerField(default=0)
	date_debut_credit = models.DateField(auto_now_add=True)
	nombre_jours_total = models.CharField(max_length=30)
	delais_recuperation = models.DateField()
	details = models.TextField()
	def __str__(self):
		return f"{self.nom_demandeur} a {self.montant} remboursable dans { self.nombre_jours_total}"

class AutresInvestissement(models.Model):
	id = models.AutoField(primary_key=True)
	nom_investissement = models.CharField(max_length=30)
	montant_investi = models.PositiveBigIntegerField()
	date_investissement = models.DateTimeField(auto_now_add=True)
	benefice = models.PositiveBigIntegerField(default=0)
	date_fin_investissement = models.DateField()


	def __str__(self):
		return f"{self.montant_investi} investi au {self.type_investissement} jusqu'au {self.date_fin_investissement}"

class VehiculesLocales(models.Model):
	id = models.AutoField(primary_key=True)
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
	id = models.AutoField(primary_key=True)
	modele = models.CharField(max_length=30)
	numero_chasis = models.CharField(max_length=70)
	prix_achat_et_transport = models.PositiveBigIntegerField(default=0)
	taux_echange = models.PositiveIntegerField(default=0)
	date_achat = models.DateTimeField(auto_now_add=True)
	date_arrivee = models.DateField()

	def __str__(self):
		return f"{self.modele} achete le {self.date_achat} arrivera le {self.date_arrivee}"

class ImportesDarEsToBuja(models.Model):
	id = models.AutoField(primary_key=True)
	Dédouanement  = models.PositiveBigIntegerField(default=0)
	transport = models.PositiveBigIntegerField(default=0)
	taux= models.PositiveIntegerField(default=0)
	autre_dépenses= models.PositiveIntegerField(default=0)
	details = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	prix_vente_previ= models.PositiveBigIntegerField(default=0)

	def __str__(self):
		return f"{self.Dédouanement} {self.taux} {self.taux} {self.prix_vente_previ}"


class Income(models.Model):
	source = models.CharField(max_length=30,blank=False)
	montant = models.PositiveBigIntegerField(default=20)
	provenance = models.CharField(max_length=30)
	is_dette = models.BooleanField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.source} {self.montant} en {self.provenance}"

class Outcome(models.Model):
	raison = models.CharField(max_length=30,blank=False)
	montant = models.PositiveBigIntegerField(default=20)
	is_dette = models.BooleanField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.raison} {self.montant} "

class Dette(models.Model):
	nom = models.CharField(max_length=30,blank=False)
	montant = models.PositiveBigIntegerField(default=20)
	date = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return f"{self.nom} {self.montant}"