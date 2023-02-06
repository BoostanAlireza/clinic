from rest_framework import serializers
from .models import PatientPersonalInfo, Medical_history, TreatmentSession


class PatientPersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPersonalInfo
        fields = ['id', 'file_number', 'first_name', 'last_name', 'father_name',
                'identification_number', 'birth_date', 'phone', 'mobile_phone']

 
class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical_history
        fields = ['ailment', 'hospitalization_history', 'hospitalization_cause', 'medication_use']


class TreatmentSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentSession
        fields = [ 'date', 'doctor', 'description', 'invoice', 'payment', 'balance']