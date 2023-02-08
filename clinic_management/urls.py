from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('patients', views.PatientPersonalInfoViewSet, basename='patient')
# router.register('medhistory', views.MedicalHistoryViewSet, basename='medical-history')
# router.register('treatsession', views.TreatmentSessionViewSet, basename='treatment-session')


patient_router = routers.NestedDefaultRouter(router, 'patients', lookup='patient')
patient_router.register('medhistory', views.MedicalHistoryViewSet,  basename='medical-history')
patient_router.register('treatmentsession', views.TreatmentSessionViewSet, basename='treatment-session')
urlpatterns = router.urls + patient_router.urls



# urlpatterns = [
#     path('clinic/', views.PatientPersonalInfoViewSet)
# ]
