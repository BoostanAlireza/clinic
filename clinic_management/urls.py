from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('patient', views.PatientPersonalInfoViewSet, basename='patient')
router.register('medhistory', views.MedicalHistoryViewSet, basename='medical-history')
router.register('treatsession', views.TreatmentSessionViewSet, basename='treatment-session')

urlpatterns = router.urls



# urlpatterns = [
#     path('clinic/', views.PatientPersonalInfoViewSet)
# ]
