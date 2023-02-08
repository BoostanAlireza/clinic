from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(PatientPersonalInfo)
admin.site.register(Medical_history)
admin.site.register(TreatmentSession)
