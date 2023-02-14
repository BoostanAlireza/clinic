from django.contrib import admin
from .models import *
# Register your models here.

class MedicalHistoryInline(admin.TabularInline):
    model = MedicalHistory

class TreatmentSessionInline(admin.TabularInline):
    model = TreatmentSession

class PatientPersonalInfoAdmin(admin.ModelAdmin):
    inlines = [MedicalHistoryInline, TreatmentSessionInline]
    list_display = ('last_name', 'first_name', 'father_name', 'file_number',
                    'identification_number', 'birth_date', 'phone', 'mobile_phone')
    list_filter = ['last_name', 'file_number', 'identification_number']
    search_fields = ['last_name', 'file_number', 'identification_number']



admin.site.register(PatientPersonalInfo, PatientPersonalInfoAdmin)
admin.site.register(MedicalHistory)
admin.site.register(TreatmentSession)
