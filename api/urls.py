from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

router = routers.DefaultRouter()

router.register("Compte_Principal", ComptePrincipalViewset)
router.register("Parcelle", ParcelleViewset)
router.register("moto", MotoViewset)
router.register("Credit", CreditViewset)
router.register("Income", IncomeViewset)
router.register("Outcome", OutcomeViewset)
router.register("Dette", DetteViewset)
router.register("autres_investssements", AutresInvestissementViewset)
router.register("vehicules_locales", VehiculesLocalesViewset)
router.register("importation_japon_to_darEsSalam", ImportesJaponToDarEsViewset)
router.register("importation_darEsSalam_to_Buja", ImportesDarEsToBujaViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
