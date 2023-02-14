from django.views.generic import TemplateView
from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views
# from . views import registration_view, welcome_view, login_view


router = routers.DefaultRouter()
router.register('patients', views.PatientPersonalInfoViewSet, basename='patient')
# router.register('clinic_management', registration_view(), basename='clinic_management')
# router.register('medhistory', views.MedicalHistoryViewSet, basename='medical-history')
# router.register('treatsession', views.TreatmentSessionViewSet, basename='treatment-session')


patient_router = routers.NestedDefaultRouter(router, 'patients', lookup='patient')
patient_router.register('medhistory', views.MedicalHistoryViewSet,  basename='patient-medicalhistory')
patient_router.register('treatmentsession', views.TreatmentSessionViewSet, basename='patient-treatmentsession')
urlpatterns = router.urls + patient_router.urls


# urlpatterns = [
#     path('', welcome_view),
#     path('authentication', login_view),
#     path('patient', registration_view),

# ]