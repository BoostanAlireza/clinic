from rest_framework import serializers
from .models import PatientPersonalInfo, MedicalHistory, TreatmentSession


class PatientPersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientPersonalInfo
        fields = ['id', 'file_number', 'first_name', 'last_name', 'father_name',
                'identification_number', 'birth_date', 'phone', 'mobile_phone']

    
class MedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ['id', 'ailment', 'hospitalization_history', 'hospitalization_cause', 'medication_use']

    def create(self, validated_data):
        patient_id = self.context['patient_id']
        return MedicalHistory.objects.create(patient_id=patient_id, **validated_data)
 



class TreatmentSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentSession
        fields = ['id', 'date', 'doctor', 'description', 'invoice', 'payment', 'balance']

    def create(self, validated_data): 
        patient_id = self.context['patient_id']
        return TreatmentSession.objects.create(patient_id=patient_id, **validated_data)