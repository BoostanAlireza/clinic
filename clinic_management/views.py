from django.shortcuts import render
from django.http import HttpResponse
from .pagination import DefaultPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import PatientPersonalInfo, MedicalHistory, TreatmentSession
from .serializers import PatientPersonalInfoSerializer, MedicalHistorySerializer, TreatmentSessionSerializer

class PatientPersonalInfoViewSet(ModelViewSet):
    queryset = PatientPersonalInfo.objects.all()
    serializer_class = PatientPersonalInfoSerializer
    pagination_class = DefaultPagination
    search_fields = ['file_number', 'identification_number', 'last_name']

    
class MedicalHistoryViewSet(ModelViewSet):
    serializer_class = MedicalHistorySerializer

    def get_queryset(self): # This is used so we don not see irrelevant data on a page
        return MedicalHistory.objects.filter(patient_id=self.kwargs['patient_pk'])

    def get_serializer_context(self): # This is for providing the id of the respective patient to the serializer
        return {'patient_id': self.kwargs['patient_pk']}



class TreatmentSessionViewSet(ModelViewSet):
    serializer_class = TreatmentSessionSerializer

    def get_queryset(self):
        return TreatmentSession.objects.filter(patient_id=self.kwargs['patient_pk'])

    def get_serializer_context(self): 
        return {'patient_id': self.kwargs['patient_pk']}


# def welcome_view(request):
#     return render(request, 'clinic_management/home.html')

# def login_view(request):
#     return render(request, 'clinic_management/login.html')

# def registration_view(request):
#     return render(request, 'clinic_management/registration.html')
