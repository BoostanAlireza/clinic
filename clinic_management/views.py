from django.shortcuts import render
from django.http import HttpResponse
from .pagination import DefaultPagination
from rest_framework.viewsets import ModelViewSet
from .models import PatientPersonalInfo, Medical_history, TreatmentSession
from .serializers import PatientPersonalInfoSerializer, MedicalHistorySerializer, TreatmentSessionSerializer
# def this_is_clinic(request):
#     return HttpResponse('Welcome to Imam reza clinic')

class PatientPersonalInfoViewSet(ModelViewSet):
    queryset = PatientPersonalInfo.objects.all()
    serializer_class = PatientPersonalInfoSerializer
    pagination_class = DefaultPagination
    # search_fields = ['file_number']

class MedicalHistoryViewSet(ModelViewSet):
    queryset = Medical_history.objects.all()
    serializer_class = MedicalHistorySerializer


class TreatmentSessionViewSet(ModelViewSet):
    queryset = TreatmentSession.objects.all()
    serializer_class = TreatmentSessionSerializer