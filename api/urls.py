from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from .views import *

router = routers.DefaultRouter()

router.register("Compte Principal", ComptePrincipalViewset)
router.register("Parcelle", ParcelleViewset)
router.register("moto", MotoViewset)
router.register("Credit", CreditViewset)
router.register("autres investssements", AutresInvestissementViewset)
router.register("vehicules locales", VehiculesLocalesViewset)
router.register("importation japon to dar-es-salam", ImportesJaponToDarEsViewset)
router.register("importation dar-es-salam to Buja", ImportesDarEsToBujaViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]
